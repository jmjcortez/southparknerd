# Generated by Django 2.2 on 2020-10-28 07:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_blog_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
