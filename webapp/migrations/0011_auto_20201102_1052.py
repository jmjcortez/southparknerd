# Generated by Django 2.2 on 2020-11-02 10:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20201102_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='temp_id',
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
