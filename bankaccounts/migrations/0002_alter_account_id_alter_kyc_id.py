# Generated by Django 4.2.4 on 2023-10-28 06:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]