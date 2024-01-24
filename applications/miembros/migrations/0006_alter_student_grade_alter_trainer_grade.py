# Generated by Django 4.2.1 on 2023-05-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("miembros", "0005_alter_customer_cipher_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="grade",
            field=models.CharField(
                choices=[
                    ("cinturon_blanco", "Cinturón Blanco"),
                    ("cinturon_amarillo", "Cinturón Amarillo"),
                    ("cinturon_naranja", "Cinturón Naranja"),
                    ("cinturon_verde", "Cinturón Verde"),
                    ("cinturon_azul", "Cinturón Azul"),
                    ("cinturon_violeta", "Cinturón Violeta"),
                    ("cinturon_rojo", "Cinturón Rojo"),
                    ("cinturon_cafe", "Cinturón Cafe"),
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
                    ("cinturon_blanco", "Cinturón Blanco"),
                    ("cinturon_amarillo", "Cinturón Amarillo"),
                    ("cinturon_naranja", "Cinturón Naranja"),
                    ("cinturon_verde", "Cinturón Verde"),
                    ("cinturon_azul", "Cinturón Azul"),
                    ("cinturon_violeta", "Cinturón Violeta"),
                    ("cinturon_rojo", "Cinturón Rojo"),
                    ("cinturon_cafe", "Cinturón Cafe"),
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
    ]
