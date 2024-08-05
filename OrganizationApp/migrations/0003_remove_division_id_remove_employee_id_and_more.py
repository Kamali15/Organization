# Generated by Django 4.1.6 on 2024-08-05 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrganizationApp', '0002_division_subdivision_remove_suborganization_org_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='division',
            name='id',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='id',
        ),
        migrations.RemoveField(
            model_name='subdivision',
            name='id',
        ),
        migrations.RemoveField(
            model_name='suborganization',
            name='id',
        ),
        migrations.AddField(
            model_name='employee',
            name='Emp_id',
            field=models.CharField(default=1, max_length=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='org_id',
            field=models.CharField(default=2, max_length=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='suborganization',
            name='sub_org_id',
            field=models.CharField(default=3, max_length=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='division',
            name='div_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='sub_div_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]