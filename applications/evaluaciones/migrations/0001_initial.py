# Generated by Django 4.2.1 on 2023-05-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Exam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(default="", max_length=45, verbose_name="Titulo"),
                ),
                (
                    "application_date",
                    models.DateTimeField(default="", verbose_name="Fecha_Aplicacion"),
                ),
                (
                    "application_place",
                    models.CharField(
                        default="", max_length=60, verbose_name="Lugar_Aplicacion"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        default="", max_length=500, verbose_name="Descripcion"
                    ),
                ),
            ],
            options={
                "verbose_name": "Examen",
                "verbose_name_plural": "Examenes",
            },
        ),
        migrations.CreateModel(
            name="ExamTrainer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "evaluator",
                    models.CharField(
                        default="", max_length=45, verbose_name="Evaluador"
                    ),
                ),
            ],
            options={
                "verbose_name": "Examen_Entrenador",
                "verbose_name_plural": "Examenes_Entrenadores",
            },
        ),
    ]