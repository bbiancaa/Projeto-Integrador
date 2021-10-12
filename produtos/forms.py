from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Produto
        fields = '__all__'
