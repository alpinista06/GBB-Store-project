# Generated by Django 3.0.14 on 2021-05-09 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0007_auto_20210429_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
