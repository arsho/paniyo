# Generated by Django 2.0.7 on 2018-07-13 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_information', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/home/cefalo/shovon/git_projects/paniyo/paniyosite/staticfiles/images/paniyo.png', upload_to=''),
        ),
    ]
