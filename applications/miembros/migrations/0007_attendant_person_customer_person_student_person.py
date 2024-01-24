# Generated by Django 4.2.1 on 2023-05-30 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("miembros", "0006_alter_student_grade_alter_trainer_grade"),
    ]

    operations = [
        migrations.AddField(
            model_name="attendant",
            name="person",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="miembros.person",
                verbose_name="Datos Personales",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customer",
            name="person",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="miembros.person",
                verbose_name="Datos Personales",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="person",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="miembros.person",
                verbose_name="Datos Personales",
            ),
            preserve_default=False,
        ),
    ]