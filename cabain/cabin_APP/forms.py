from django import forms
from cabin_APP.models import Region, City, User, Project, PaymentMethod, MeasureUnit

class FormRegion(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'

class FormCity(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

class FormUserLogin(forms.ModelForm):
    class Meta:
        model = User
        widgets ={
            'password': forms.PasswordInput()
        }
        fields = ['username', 'password']


class FormUserRegistration(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput()
        }
        fields = '__all__'

class FormCreateProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'surface', 'total_price']

    
class FormPaymenMethod(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class FormUnidadMedida(forms.ModelForm):
    class Meta:
        model = MeasureUnit
        fields = '__all__'
