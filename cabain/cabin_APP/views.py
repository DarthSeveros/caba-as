from django.shortcuts import render, redirect
from cabin_APP.forms import FormRegion, FormCity, FormUserLogin, FormUserRegistration, FormCreateProject, FormPaymentMethod, FormUnidadMedida, FormWorker
from cabin_APP.models import Region, City, User, Project, PaymentMethod, MeasureUnit, Worker

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
                    return main_menu(request, user_consult.getId())  
    context = {'form' : form}
    return render(request, 'login.html', context)

def resgistrar_usuario(request):
    form = FormUserRegistration()
    if request.method == 'POST':
        form = FormUserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect(iniciar_sesion)
    context = {'form': form}
    return render(request, 'registro.html', context)

def crear_proyecto(request, userId):
    form = FormCreateProject()
    form.fields['username'].initial = userId
    if request.method == 'POST':
        form = FormCreateProject(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listado_proyectos)
    context = {'form': form}
    return render(request, 'proyecto_nuevo.html', context)

def listado_proyectos(request):
    proyectos = Project.objects.all()
    context = {'proyectos': proyectos}
    return render(request, 'listado_proyectos.html', context)

def main_menu(request, userId):
    context = {'usuario': userId}
    return render(request, 'menu_principal.html', context)

def payment_method(request):
    form = FormPaymentMethod()
    if request.method == 'POST':
        form = FormPaymentMethod(request.POST)
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
    metodo = PaymentMethod.objects.get(id=id)
    form = FormPaymentMethod(instance=metodo)
    if request.method == 'POST':
        form = FormPaymentMethod(request.POST, instance=metodo)
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

def maestro(request):
    form = FormWorker()
    maestros = Worker.objects.all()
    if request.method == 'POST':
        form = FormWorker(request.POST)
        if form.is_valid():
            form.save()
            return redirect(maestro)
    context = {
        'form': form,
        'maestros': maestros
        }
    return render(request, 'maestro.html', context)

def actualizar_maestro(request, id):
    worker = Worker.objects.get(id=id)
    form = FormWorker(instance=worker)
    if request.method == 'POST':
        form = FormWorker(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            return redirect(maestro)
    context = {'form': form}
    return render(request, 'actualizar_maestro.html', context)

def eliminar_maestro(request, id):
    worker = Worker.objects.get(id=id)
    worker.delete()
    return redirect(maestro)
