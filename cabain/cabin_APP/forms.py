from django import forms
from cabin_APP.models import Region, City

class FormRegion(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'

class FormCity(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

