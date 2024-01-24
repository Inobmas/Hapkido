# Generated by Django 4.2.1 on 2023-05-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Campus",
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
                    "name",
                    models.CharField(default="", max_length=60, verbose_name="Nombre"),
                ),
                (
                    "address",
                    models.CharField(
                        default="", max_length=40, verbose_name="Direccion"
                    ),
                ),
            ],
            options={
                "verbose_name": "Sede",
                "verbose_name_plural": "Sedes",
            },
        ),
        migrations.CreateModel(
            name="Group",
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
                    "name",
                    models.CharField(default="", max_length=30, verbose_name="Nombre"),
                ),
                (
                    "code",
                    models.CharField(default="", max_length=30, verbose_name="Codigo"),
                ),
            ],
            options={
                "verbose_name": "Grupo",
                "verbose_name_plural": "Grupos",
            },
        ),
        migrations.CreateModel(
            name="TimeZone",
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
                ("day", models.DateTimeField(verbose_name="Dia")),
                ("hour", models.DateTimeField(verbose_name="Hora")),
            ],
            options={
                "verbose_name": "Franja_Horaria",
                "verbose_name_plural": "Franjas_Horarias",
            },
        ),
        migrations.CreateModel(
            name="TimeZoneGroup",
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
                    "coach_in_charge",
                    models.CharField(
                        default="", max_length=30, verbose_name="Entrenador_Encargado"
                    ),
                ),
            ],
            options={
                "verbose_name": "Grupo_Franja_Horaria",
                "verbose_name_plural": "Grupos_Franjas_Horarias",
            },
        ),
        migrations.CreateModel(
            name="Training",
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
                    "training_type",
                    models.CharField(
                        default="", max_length=30, verbose_name="Tipo_Entrenamiento"
                    ),
                ),
            ],
            options={
                "verbose_name": "Entrenamiento",
                "verbose_name_plural": "Entrenamientos",
            },
        ),
    ]
