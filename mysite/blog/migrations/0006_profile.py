# Generated by Django 2.2.1 on 2019-05-25 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190525_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.bmp', upload_to='profile_pics')),
                ('description', models.TextField()),
                ('phone_no', models.CharField(max_length=100)),
            ],
        ),
    ]