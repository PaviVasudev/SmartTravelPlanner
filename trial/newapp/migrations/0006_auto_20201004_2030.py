# Generated by Django 3.1.2 on 2020-10-04 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_auto_20201004_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertravel',
            name='name',
            field=models.CharField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='usertravel',
            name='places',
            field=models.TextField(default='', max_length=1000, null=True),
        ),
    ]
