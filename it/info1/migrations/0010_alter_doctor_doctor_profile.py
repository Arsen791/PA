# Generated by Django 4.1.2 on 2023-04-16 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info1', '0009_alter_doctor_doctor_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_profile',
            field=models.BooleanField(help_text=True, null=True),
        ),
    ]