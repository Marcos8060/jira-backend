# Generated by Django 4.2.2 on 2023-06-25 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_todos_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.project'),
        ),
    ]