# Generated by Django 2.1 on 2018-09-20 12:08

from django.db import migrations

def add_params(apps, schema_editor):
    Parameter = apps.get_model('whip','Parameter')

    # Cuisine Types 
    # https://www.bbcgoodfood.com/recipes/category/cuisines
    Parameter.objects.create(key ="Cuisine Type",value="American")
    Parameter.objects.create(key ="Cuisine Type",value="British")
    Parameter.objects.create(key ="Cuisine Type",value="Caribbean")
    Parameter.objects.create(key ="Cuisine Type",value="Chinese")
    Parameter.objects.create(key ="Cuisine Type",value="French")
    Parameter.objects.create(key ="Cuisine Type",value="Greek")
    Parameter.objects.create(key ="Cuisine Type",value="Indian")
    Parameter.objects.create(key ="Cuisine Type",value="Italian")
    Parameter.objects.create(key ="Cuisine Type",value="Japanese")
    Parameter.objects.create(key ="Cuisine Type",value="Mediterranean")
    Parameter.objects.create(key ="Cuisine Type",value="Mexican")
    Parameter.objects.create(key ="Cuisine Type",value="Moroccan")
    Parameter.objects.create(key ="Cuisine Type",value="Spanish")
    Parameter.objects.create(key ="Cuisine Type",value="Thai")
    Parameter.objects.create(key ="Cuisine Type",value="Turkish")
    Parameter.objects.create(key ="Cuisine Type",value="Vietnamese")

class Migration(migrations.Migration):

    dependencies = [
        ('whip', '0003_import_parameters'),
    ]

    operations = [
        migrations.RunPython(add_params)
    ]
