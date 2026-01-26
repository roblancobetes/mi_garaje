from django.shortcuts import get_object_or_404, render
from .models import Coche


def lista_coches(request):
    coches = Coche.objects.all()
    return render(request, "garaje/lista_coches.html", {"coches": coches})


def detalle_coche(request, pk: int):
    coche = get_object_or_404(Coche, pk=pk)
    return render(request, "garaje/detalle_coche.html", {"coche": coche})
