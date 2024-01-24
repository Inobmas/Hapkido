# Generated by Django 4.2.1 on 2023-05-30 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("miembros", "0003_alter_trainer_person"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="grade",
            field=models.CharField(
                choices=[
                    ("cinturon_blanco", "Cinturon Blanco"),
                    ("cinturon_amarillo", "Cinturon Amarillo"),
                    ("cinturon_naranja", "Cinturon Naranja"),
                    ("cinturon_verde", "Cinturon Verde"),
                    ("cinturon_azul", "Cinturon Azul"),
                    ("cinturon_violeta", "Cinturon Violeta"),
                    ("cinturon_rojo", "Cinturon Rojo"),
                    ("cinturon_cafe", "Cinturon Cafe"),
                    ("instructor", "Instructor"),
                    ("instructor_mayor", "Instructor Mayor"),
                    ("profesor", "Profesor"),
                    ("maestro", "Maestro"),
                    ("gran_maestro", "Gran Maestro"),
                ],
                default="cinturon_blanco",
                max_length=20,
                verbose_name="Rango/Grado",
            ),
        ),
        migrations.AlterField(
            model_name="trainer",
            name="grade",
            field=models.CharField(
                choices=[
                    ("cinturon_blanco", "Cinturon Blanco"),
                    ("cinturon_amarillo", "Cinturon Amarillo"),
                    ("cinturon_naranja", "Cinturon Naranja"),
                    ("cinturon_verde", "Cinturon Verde"),
                    ("cinturon_azul", "Cinturon Azul"),
                    ("cinturon_violeta", "Cinturon Violeta"),
                    ("cinturon_rojo", "Cinturon Rojo"),
                    ("cinturon_cafe", "Cinturon Cafe"),
                    ("instructor", "Instructor"),
                    ("instructor_mayor", "Instructor Mayor"),
                    ("profesor", "Profesor"),
                    ("maestro", "Maestro"),
                    ("gran_maestro", "Gran Maestro"),
                ],
                default="cinturon_blanco",
                max_length=20,
                verbose_name="Rango/Grado",
            ),
        ),
        migrations.AlterField(
            model_name="trainer",
            name="person",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="miembros.person",
                verbose_name="Datos",
            ),
        ),
    ]