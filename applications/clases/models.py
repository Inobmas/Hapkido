from django.db import models


class Group(models.Model):
    name = models.CharField(
        "Nombre", max_length=30, blank=False, null=False, default=""
    )
    code = models.CharField(
        "Codigo", max_length=30, blank=False, null=False, default=""
    )

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"

    def __str__(self):
        return f"{self.name}{self.code}"


class TimeZone(models.Model):
    day = models.DateTimeField("Dia")
    hour = models.DateTimeField("Hora")

    class Meta:
        verbose_name = "Franja_Horaria"
        verbose_name_plural = "Franjas_Horarias"

    def __str__(self):
        return f"{self.day}{self.hour}"


class TimeZoneGroup(models.Model):
    coach_in_charge = models.CharField(
        "Entrenador_Encargado", max_length=30, blank=False, null=False, default=""
    )

    class Meta:
        verbose_name = "Grupo_Franja_Horaria"
        verbose_name_plural = "Grupos_Franjas_Horarias"

    def __str__(self):
        return f"{self.coach_in_charge}"


class Training(models.Model):
    training_type = models.CharField("Tipo_Entrenamiento", max_length=30, default="")

    class Meta:
        verbose_name = "Entrenamiento"
        verbose_name_plural = "Entrenamientos"

    def __str__(self):
        return f"{self.training_type}"


class Campus(models.Model):
    name = models.CharField(
        "Nombre", max_length=60, blank=False, null=False, default=""
    )
    address = models.CharField(
        "Direccion", max_length=40, blank=False, null=False, default=""
    )

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"

    def __str__(self):
        return f"{self.name}{self.address}"
