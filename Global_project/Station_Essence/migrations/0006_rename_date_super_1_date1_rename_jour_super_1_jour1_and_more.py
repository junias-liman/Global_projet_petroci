# Generated by Django 5.1.5 on 2025-01-26 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Station_Essence', '0005_rename_litre_super_1_jour_rename_litre_super_2_jour_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super_1',
            old_name='date',
            new_name='date1',
        ),
        migrations.RenameField(
            model_name='super_1',
            old_name='jour',
            new_name='jour1',
        ),
        migrations.RenameField(
            model_name='super_1',
            old_name='quantite',
            new_name='quantite1',
        ),
        migrations.RenameField(
            model_name='super_1',
            old_name='valeur',
            new_name='valeur1',
        ),
        migrations.RenameField(
            model_name='super_1',
            old_name='veille',
            new_name='veille1',
        ),
        migrations.RenameField(
            model_name='super_2',
            old_name='date',
            new_name='date2',
        ),
        migrations.RenameField(
            model_name='super_2',
            old_name='jour',
            new_name='jour2',
        ),
        migrations.RenameField(
            model_name='super_2',
            old_name='quantite',
            new_name='quantite2',
        ),
        migrations.RenameField(
            model_name='super_2',
            old_name='valeur',
            new_name='valeur2',
        ),
        migrations.RenameField(
            model_name='super_2',
            old_name='veille',
            new_name='veille2',
        ),
        migrations.RenameField(
            model_name='super_3',
            old_name='date',
            new_name='date3',
        ),
        migrations.RenameField(
            model_name='super_3',
            old_name='jour',
            new_name='jour3',
        ),
        migrations.RenameField(
            model_name='super_3',
            old_name='quantite',
            new_name='quantite3',
        ),
        migrations.RenameField(
            model_name='super_3',
            old_name='valeur',
            new_name='valeur3',
        ),
        migrations.RenameField(
            model_name='super_3',
            old_name='veille',
            new_name='veille3',
        ),
        migrations.RenameField(
            model_name='super_4',
            old_name='date',
            new_name='date4',
        ),
        migrations.RenameField(
            model_name='super_4',
            old_name='jour',
            new_name='jou4r',
        ),
        migrations.RenameField(
            model_name='super_4',
            old_name='quantite',
            new_name='quantite4',
        ),
        migrations.RenameField(
            model_name='super_4',
            old_name='valeur',
            new_name='valeur4',
        ),
        migrations.RenameField(
            model_name='super_4',
            old_name='veille',
            new_name='veille4',
        ),
    ]
