# Generated by Django 2.2.1 on 2019-05-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='image',
            field=models.ImageField(default='default.bmp', upload_to='city_pics'),
        ),
    ]
