# Generated by Django 4.1.2 on 2023-04-22 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info1', '0021_alter_user_birth_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_infos', to='info1.user_name'),
        ),
    ]