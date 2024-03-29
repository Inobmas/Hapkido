# Generated by Django 4.2.1 on 2023-05-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attendant",
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
                    "relationship",
                    models.CharField(
                        default="", max_length=20, verbose_name="Parentesco"
                    ),
                ),
            ],
            options={
                "verbose_name": "Acudiente",
                "verbose_name_plural": "Acudientes",
            },
        ),
        migrations.CreateModel(
            name="Customer",
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
                    "cipher",
                    models.CharField(default="", max_length=30, verbose_name="Codigo"),
                ),
            ],
            options={
                "verbose_name": "Cliente",
                "verbose_name_plural": "Clientes",
            },
        ),
        migrations.CreateModel(
            name="Person",
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
                ("name", models.CharField(max_length=30, verbose_name="Nombres")),
                (
                    "last_name",
                    models.CharField(max_length=30, verbose_name="Apellidos"),
                ),
                (
                    "identity_name",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="Nombre_identitario",
                    ),
                ),
                (
                    "document_type",
                    models.CharField(
                        choices=[
                            ("cedula_ciudadania", "CC"),
                            ("cedula_extranjeria", "CE"),
                            ("pasaporte", "PP"),
                            ("tarjeta_identidad", "TI"),
                            ("registro_civil", "RC"),
                        ],
                        default="cedula_ciudadania",
                        max_length=20,
                        verbose_name="Tipo_documento",
                    ),
                ),
                (
                    "document_number",
                    models.CharField(
                        default="", max_length=15, verbose_name="Numero_documento"
                    ),
                ),
                ("age", models.IntegerField(verbose_name="Edad")),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("hombre", "Hombre"), ("mujer", "Mujer")],
                        default="",
                        max_length=10,
                        null=True,
                        verbose_name="Genero",
                    ),
                ),
                (
                    "cell_phone",
                    models.CharField(default="", max_length=15, verbose_name="Celular"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=60, null=True, verbose_name="correo_electronico"
                    ),
                ),
                (
                    "photo",
                    models.ImageField(null=True, upload_to="", verbose_name="Foto"),
                ),
                (
                    "fingerprint",
                    models.ImageField(null=True, upload_to="", verbose_name="Huella"),
                ),
                (
                    "residence_adress",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=40,
                        null=True,
                        verbose_name="Direccion_residencia",
                    ),
                ),
                (
                    "ethnicity",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=20,
                        null=True,
                        verbose_name="Etnia",
                    ),
                ),
                (
                    "profession",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=30,
                        null=True,
                        verbose_name="Profesion",
                    ),
                ),
                (
                    "occupation",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=30,
                        null=True,
                        verbose_name="Ocupacion",
                    ),
                ),
                (
                    "disability",
                    models.BooleanField(
                        blank=True, default=False, verbose_name="Discapacidad"
                    ),
                ),
                (
                    "description_disability",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=500,
                        null=True,
                        verbose_name="Descripcion_discapacidad",
                    ),
                ),
                (
                    "observations",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=500,
                        null=True,
                        verbose_name="Observaciones",
                    ),
                ),
            ],
            options={
                "verbose_name": "Persona",
                "verbose_name_plural": "Personas",
            },
        ),
        migrations.CreateModel(
            name="Student",
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
                    "grade",
                    models.CharField(
                        choices=[
                            ("cinturon_blanco", "Cinturon_Blanco"),
                            ("cinturon_amarillo", "Cinturon_Amarillo"),
                            ("cinturon_naranja", "Cinturon_Naranja"),
                            ("cinturon_verde", "Cinturon_Verde"),
                            ("cinturon_azul", "Cinturon_Azul"),
                            ("cinturon_violeta", "Cinturon_Violeta"),
                            ("cinturon_rojo", "Cinturon_Rojo"),
                            ("cinturon_cafe", "Cinturon_Cafe"),
                            ("instructor", "Instructor"),
                            ("instructor_mayor", "Instructor_Mayor"),
                            ("profesor", "Profesor"),
                            ("maestro", "Maestro"),
                            ("gran_maestro", "Gran_Maestro"),
                        ],
                        default="cinturon_blanco",
                        max_length=20,
                        verbose_name="Rango/Grado",
                    ),
                ),
            ],
            options={
                "verbose_name": "Alumno",
                "verbose_name_plural": "Alumnos",
            },
        ),
        migrations.CreateModel(
            name="Trainer",
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
                    "grade",
                    models.CharField(
                        choices=[
                            ("cinturon_blanco", "Cinturon_Blanco"),
                            ("cinturon_amarillo", "Cinturon_Amarillo"),
                            ("cinturon_naranja", "Cinturon_Naranja"),
                            ("cinturon_verde", "Cinturon_Verde"),
                            ("cinturon_azul", "Cinturon_Azul"),
                            ("cinturon_violeta", "Cinturon_Violeta"),
                            ("cinturon_rojo", "Cinturon_Rojo"),
                            ("cinturon_cafe", "Cinturon_Cafe"),
                            ("instructor", "Instructor"),
                            ("instructor_mayor", "Instructor_Mayor"),
                            ("profesor", "Profesor"),
                            ("maestro", "Maestro"),
                            ("gran_maestro", "Gran_Maestro"),
                        ],
                        default="cinturon_blanco",
                        max_length=20,
                        verbose_name="Rango/Grado",
                    ),
                ),
                (
                    "review",
                    models.CharField(
                        blank=True, max_length=1000, null=True, verbose_name="Reseña"
                    ),
                ),
            ],
            options={
                "verbose_name": "Entrenador",
                "verbose_name_plural": "Entrenadores",
            },
        ),
    ]
