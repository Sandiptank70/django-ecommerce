# Generated by Django 3.1.1 on 2020-09-27 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20200927_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='catagory',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=2000),
        ),
    ]
