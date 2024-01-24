from django.db import models


class Exam(models.Model):
    title = models.CharField("Titulo", max_length=45, default="")
    application_date = models.DateTimeField("Fecha_Aplicacion", default="")
    application_place = models.CharField("Lugar_Aplicacion", max_length=60, default="")
    description = models.CharField("Descripcion", max_length=500, default="")

    class Meta:
        verbose_name = "Examen"
        verbose_name_plural = "Examenes"

    def __str__(self):
        return f"{self.title}{self.application_day}{self.application_hour}"


class ExamTrainer(models.Model):
    evaluator = models.CharField("Evaluador", max_length=45, default="")

    class Meta:
        verbose_name = "Examen_Entrenador"
        verbose_name_plural = "Examenes_Entrenadores"

    def __str__(self):
        return f"{self.evaluator}"
