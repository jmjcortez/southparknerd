# Generated by Django 2.2 on 2020-10-30 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_add_new_synopsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='characters',
            field=models.ManyToManyField(null=True, to='webapp.Character'),
        ),
    ]
