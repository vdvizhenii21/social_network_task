# Generated by Django 4.2.1 on 2023-06-02 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_remove_useractivity_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='useractivity', to=settings.AUTH_USER_MODEL),
        ),
    ]