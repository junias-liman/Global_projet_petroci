# Generated by Django 5.1.5 on 2025-01-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Station_Essence', '0014_alter_super_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gazoil',
            name='type',
            field=models.IntegerField(),
        ),
    ]
