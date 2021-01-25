# Generated by Django 3.1.5 on 2021-01-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/media/images/teste.jpeg', upload_to='images/'),
        ),
    ]
