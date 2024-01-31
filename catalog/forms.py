from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('__all__')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        closed_names = 'казино,криптовалюта,крипта,биржа,дешево,бесплатно,обман,полиция,радар'
        closed_names = closed_names.split(',')
        if cleaned_data in closed_names:
            raise forms.ValidationError('Ошибка имени пользователя')
        return cleaned_data

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('__all__')