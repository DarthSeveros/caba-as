from django.shortcuts import render, redirect
from cabin_APP.forms import FormCreateProject, FormPaymentMethod, FormUnidadMedida, FormWorker
from cabin_APP.models import Region, City, Project, PaymentMethod, MeasureUnit, Worker
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def crear_proyecto(request):
    form = FormCreateProject(initial={'username': request.user})
    if request.method == 'POST':
        form = FormCreateProject(request.POST, initial={'username': request.user})
        if request.user.id != form.data['username']:
            return redirect(crear_proyecto)
        if form.is_valid():
            form.save()
            return redirect(listado_proyectos)
    context = {'form': form}
    return render(request, 'proyecto_nuevo.html', context)

@login_required
def listado_proyectos(request):
    proyectos = Project.objects.filter(username=request.user)
    context = {'proyectos': proyectos}
    return render(request, 'listado_proyectos.html', context)

@login_required
def main_menu(request):
    return render(request, 'menu_principal.html')

@login_required
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

@login_required
def eliminar_metodo_pago(request, id):
    metodo = PaymentMethod.objects.get(id=id)
    metodo.delete()
    return redirect(payment_method)

@login_required
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

@login_required
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

@login_required
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

@login_required    
def eliminar_unidad_medida(request, id):
    unidad = MeasureUnit.objects.get(id=id)
    unidad.delete()
    return redirect(unidad_medida)

@login_required
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

@login_required
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

@login_required
def eliminar_maestro(request, id):
    worker = Worker.objects.get(id=id)
    worker.delete()
    return redirect(maestro)

@login_required
def sessions(request):
    auto = request.session['auto']
    print(auto)
    return redirect(maestro)
