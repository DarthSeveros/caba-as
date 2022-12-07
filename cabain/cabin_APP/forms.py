from django import forms
from cabin_APP.models import Client, BillDetail, Product, Region, City, Project, PaymentMethod, MeasureUnit, Worker, Bill

class FormRegion(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'

class FormCity(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

class FormCreateProject(forms.ModelForm):
    class Meta:
        model = Project
        widgets = {
            'username': forms.HiddenInput
        }
        fields = '__all__'
    
class FormPaymentMethod(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class FormUnidadMedida(forms.ModelForm):
    class Meta:
        model = MeasureUnit
        fields = '__all__'

class FormWorker(forms.ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'

class FormProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class FormBill(forms.ModelForm):
    class Meta:
        model = Bill
        widgets = {
            'username': forms.HiddenInput
        }
        fields = '__all__'

class FormBillDetail(forms.ModelForm):
    class Meta:
        model = BillDetail
        fields = '__all__'

class FormClient(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'