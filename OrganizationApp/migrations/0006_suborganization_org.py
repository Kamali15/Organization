# Generated by Django 4.1.6 on 2024-08-05 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrganizationApp', '0005_remove_suborganization_org_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='suborganization',
            name='org',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='OrganizationApp.organization'),
            preserve_default=False,
        ),
    ]
