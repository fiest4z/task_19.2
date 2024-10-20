from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    forbidden_words = [
        "казино", "криптовалюта", "крипта",
        "биржа", "дешево", "бесплатно",
        "обман", "полиция", "радар"
    ]

    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите наименование товара",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите описание товара",
                }
            ),
            "preview": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"})
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if any(word in name.lower() for word in self.forbidden_words):
            raise ValidationError(
                "Название товара не должно содержать запрещенные слова"
            )
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if any(word in description.lower() for word in self.forbidden_words):
            raise ValidationError("Описание не должно содержать запрещенные слова")
        return description


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
        widgets = {
            "product": forms.Select(attrs={"class": "form-select"}),
            "version_number": forms.TextInput(attrs={"class": "form-control"}),
            "version_name": forms.TextInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("description", "category", "is_published")
        widgets = {
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите описание товара",
                }
            ),
            "category": forms.Select(attrs={"class": "form-select"}),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
