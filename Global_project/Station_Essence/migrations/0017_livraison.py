# Generated by Django 5.1.5 on 2025-01-28 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Station_Essence', '0016_essence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('valeur', models.IntegerField()),
                ('date', models.DateField()),
                ('Cuve', models.CharField(max_length=50)),
            ],
        ),
    ]
