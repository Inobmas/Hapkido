# Generated by Django 4.2.1 on 2023-05-31 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("miembros", "0007_attendant_person_customer_person_student_person"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="attendant",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="miembros.attendant",
            ),
            preserve_default=False,
        ),
    ]
