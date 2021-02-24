# Generated by Django 3.1.6 on 2021-02-23 23:27

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='middag',
            name='allergener',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('GLUTEN', 'Gluten'), ('LAKTOSE', 'Laktose'), ('EGG', 'Egg'), ('NØTTER', 'Nøtter')], default=None, max_length=25),
        ),
    ]