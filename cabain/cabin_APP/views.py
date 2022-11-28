from django.shortcuts import render, redirect
from cabin_APP.forms import FormRegion, FormCity, FormUserLogin, FormUserRegistration, FormCreateProject, FormPaymenMethod, FormUnidadMedida
from cabin_APP.models import Region, City, User, Project, PaymentMethod, MeasureUnit

# Create your views here.

def listado_regiones(request):
    regiones = Region.objects.all()
    context = {'regiones': regiones}
    return render(request, 'regiones.html', context)

def ingresar_region(request):
    form = FormRegion()
    if request.method == 'POST':
        form = FormRegion(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listado_regiones)
    context = {'form': form}
    return render(request, 'ingresar_region.html', context)

def listado_ciudades(request):
    ciudades = City.objects.all()
    context = {'ciudades': ciudades}
    return render(request, 'ciudades.html', context)

def ingresar_ciudades(request):
    form = FormCity()
    if request.method == 'POST':
        form = FormCity(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listado_ciudades)
    context = {'form': form}
    return render(request, 'ingresar_ciudad.html', context)

def iniciar_sesion(request):
    form = FormUserLogin()
    if request.method == 'POST':
        form = FormUserLogin(request.POST)
        if form.is_valid():
            user = form.data['username']
            password = form.data['password']
            if User.objects.filter(username=user).exists():
                user_consult = User.objects.get(username=user)
                if (user, password) == user_consult.getToLogin():
                    return redirect(main_menu)  
    context = {'form' : form}
    return render(request, 'login.html', context)

def resgistrar_usuario(request):
    form = FormUserRegistration()
    if request.method == 'POST':
        form = FormUserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect(main_menu)
    context = {'form': form}
    return render(request, 'registro.html', context)

def crear_proyecto(request):
    form = FormCreateProject()
    if request.method == 'POST':
        form = FormCreateProject(request.POST)
        if form.is_valid():
            form.save()
            return redirect()
    context = {'form': form}
    return render(request, 'proyecto_nuevo.html', context)

def main_menu(request):
    return render(request, 'menu_principal.html')

def payment_method(request):
    form = FormPaymenMethod()
    if request.method == 'POST':
        form = FormPaymenMethod(request.POST)
        if form.is_valid():
            form.save()
            return redirect(payment_method)
    metodos = PaymentMethod.objects.all()
    context = {
        'form': form,
        'metodos': metodos
        }
    return render(request, 'metodo_pago.html', context)

def eliminar_metodo_pago(request, id):
    metodo = PaymentMethod.objects.get(id=id)
    metodo.delete()
    return redirect(payment_method)

def actualizar_metodo_pago(request, id):
    form = PaymentMethod()
    metodo = PaymentMethod.objects.get(id=id)
    if request.method == 'POST':
        form = PaymentMethod(instance=metodo)
        if form.is_valid():
            form.save()
            return redirect(payment_method)
    metodos = PaymentMethod.objects.all()
    context = {
        'form': form,
        'metodos': metodos
    }
    return render(request, 'actualizar_metodo_pago.html', context)

def unidad_medida(request):
    form = FormUnidadMedida()
    if request.method == 'POST':
        form = FormUnidadMedida(request.POST)
        if form.is_valid():
            form.save()
            return redirect(unidad_medida)
    unidades = MeasureUnit.objects.all()
    context = {
        'form': form,
        'unidades': unidades
    }
    return render(request, 'unidadMedida.html', context)

def actualizar_unidad_medida(request, id):
    unidad = MeasureUnit.objects.get(id = id)
    form = FormUnidadMedida(instance=unidad)
    if request.method == 'POST':
        form = FormUnidadMedida(request.POST, instance=unidad)
        if form.is_valid():
            form.save()
            return redirect(unidad_medida)
    unidades = MeasureUnit.objects.all()
    context = {
        'form': form,
        'unidades': unidades
    }
    return render(request, 'editar_unidadMedida.html', context)
    
def eliminar_unidad_medida(request, id):
    unidad = MeasureUnit.objects.get(id=id)
    unidad.delete()
    return redirect(unidad_medida)