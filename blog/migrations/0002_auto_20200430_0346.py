# Generated by Django 3.0.5 on 2020-04-30 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
