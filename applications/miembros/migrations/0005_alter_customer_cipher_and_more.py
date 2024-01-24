# Generated by Django 4.2.1 on 2023-05-30 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("miembros", "0004_alter_student_grade_alter_trainer_grade_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="cipher",
            field=models.CharField(default="", max_length=30, verbose_name="Código"),
        ),
        migrations.AlterField(
            model_name="person",
            name="description_disability",
            field=models.CharField(
                blank=True,
                default="",
                max_length=500,
                null=True,
                verbose_name="Descripción Discapacidad",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="document_number",
            field=models.CharField(
                default="", max_length=15, verbose_name="Número Documento"
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="document_type",
            field=models.CharField(
                choices=[
                    ("cedula_ciudadania", "CC"),
                    ("cedula_extranjeria", "CE"),
                    ("pasaporte", "PP"),
                    ("tarjeta_identidad", "TI"),
                    ("registro_civil", "RC"),
                ],
                default="cedula_ciudadania",
                max_length=20,
                verbose_name="Tipo documento",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="email",
            field=models.EmailField(
                max_length=60, null=True, verbose_name="Correo Electrónico"
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("hombre", "Hombre"), ("mujer", "Mujer")],
                default="",
                max_length=10,
                null=True,
                verbose_name="Género",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="identity_name",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Nombre identitario"
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="occupation",
            field=models.CharField(
                blank=True,
                default="",
                max_length=30,
                null=True,
                verbose_name="Ocupación",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="profession",
            field=models.CharField(
                blank=True,
                default="",
                max_length=30,
                null=True,
                verbose_name="Profesión",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="residence_adress",
            field=models.CharField(
                blank=True,
                default="",
                max_length=40,
                null=True,
                verbose_name="Dirección Residencia",
            ),
        ),
        migrations.AlterField(
            model_name="trainer",
            name="person",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="miembros.person",
                verbose_name="Datos Personales",
            ),
        ),
    ]