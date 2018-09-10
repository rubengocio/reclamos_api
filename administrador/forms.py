from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe

from api.models import Reclamo, Subcategoria

class ImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            t = value
            output.append('<img src="{}">'.format(t.url))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class ReclamoForm(forms.ModelForm):
    subcategoria = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Subcategoria.objects.all())
    imagen = forms.ImageField(widget=ImageWidget)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    calle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
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
            'coord_x',
            'coord_y',
            'estado'
        )
