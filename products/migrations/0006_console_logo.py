# Generated by Django 2.0.7 on 2018-08-05 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_brand_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='console',
            name='logo',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]