# Generated by Django 4.1.2 on 2023-01-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_manage_drugs_unit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Manage',
        ),
        migrations.AddField(
            model_name='manageinfo',
            name='system_name',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
