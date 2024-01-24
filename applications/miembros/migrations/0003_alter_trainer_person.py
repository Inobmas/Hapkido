# Generated by Django 4.2.1 on 2023-05-30 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("miembros", "0002_trainer_person"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trainer",
            name="person",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="miembros.person",
            ),
            preserve_default=False,
        ),
    ]