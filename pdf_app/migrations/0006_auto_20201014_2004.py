# Generated by Django 3.1.2 on 2020-10-14 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_app', '0005_document_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='task_id',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True, unique=True),
        ),
    ]
