# Generated by Django 2.0 on 2017-12-18 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0006_cocktail_abc'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='bgh',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]