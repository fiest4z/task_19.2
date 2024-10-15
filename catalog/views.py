from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.mixins import CustomLoginRequiredMixin
from catalog.models import Product, Version


# Create your views here.

class ProductListView(ListView):
    model = Product


class ProductCreateView(CustomLoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Создание товара"
        VersionFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(self.request.POST)
        else:
            context_data["formset"] = VersionFormset()
        return context_data

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context["formset"]
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Редактирование товара"
        VersionFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1, can_delete=True
        )
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["formset"]
        if form.is_valid() and formset.is_valid():
            versions = [
                form for form in formset if form.cleaned_data.get("is_active", False)
            ]
            if len(versions) > 1:
                form.add_error(
                    None, "У продукта не может быть более одной активной версии."
                )
                return self.form_invalid(form)
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        return self.form_invalid(form)


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
