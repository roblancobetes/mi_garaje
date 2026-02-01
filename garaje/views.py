from django.shortcuts import get_object_or_404, render, redirect
from .models import Coche
from .forms import formularioNuevoCoche
from datetime import datetime


def lista_coches(request):
    coches = Coche.objects.all()
    return render(request, "garaje/lista_coches.html", {"coches": coches})


def detalle_coche(request, pk: int):
    coche = get_object_or_404(Coche, pk=pk)
    return render(request, "garaje/detalle_coche.html", {"coche": coche})

def formulario_coche(request):

    form = formularioNuevoCoche()

    if request.method == 'POST':

        form = formularioNuevoCoche(request.POST)

        if form.is_valid():

            Coche.objects.create(
                marca=form.cleaned_data["marca"],
                modelo=form.cleaned_data["modelo"],
                dueno=form.cleaned_data["dueno"],
                created_at = datetime.now()
            )

            return redirect('garaje:lista')
        
        else:
            form.add_error(None, "Introduzca unos parámetros válidos")

    else:
        return render(request, 'garaje/nuevo_coche.html', {
        'form': form
    })
