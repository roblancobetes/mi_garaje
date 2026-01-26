from django.db import models


class Coche(models.Model):
    marca = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
    dueno = models.CharField(max_length=120)  # simple: nombre del dueño

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["marca", "modelo", "dueno"]

    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} — {self.dueno}"
