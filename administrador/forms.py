from django import forms

from api.models import Reclamo, Subcategoria


class ReclamoForm(forms.ModelForm):
    subcategoria = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Subcategoria.objects.all())
    imagen = forms.ImageField(required=False)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    calle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    coord_x = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    coord_y = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    estado = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=Reclamo.ESTADOS_PEDIDO_CHOICES)

    class Meta:
        model = Reclamo
        fields = (
            'subcategoria',
            'imagen',
            'descripcion',
            'calle',
            'numero',
            'coord_x',
            'coord_y',
            'estado'
        )
