# Generated by Django 2.0.1 on 2018-01-14 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='dueDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='datedue for todo task'),
        ),
    ]
