# Generated by Django 4.1.7 on 2023-03-25 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(default='https://www.ncenet.com/wp-content/uploads/2020/04/no-image-png-2.png', max_length=1024, null=True, verbose_name='Image'),
        ),
    ]
