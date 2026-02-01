from django.urls import path
from . import views

app_name = "garaje"

urlpatterns = [
    path("", views.lista_coches, name="lista"),
    path("coche/<int:pk>/", views.detalle_coche, name="detalle"),
    path("nuevo-coche", views.formulario_coche, name = "nuevo_coche")
]
