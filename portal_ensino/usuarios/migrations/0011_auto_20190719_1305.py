# Generated by Django 2.2.3 on 2019-07-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_delete_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='foto',
            field=models.ImageField(blank=True, default='default.jpeg', null=True, upload_to='fotos/profile'),
        ),
    ]
