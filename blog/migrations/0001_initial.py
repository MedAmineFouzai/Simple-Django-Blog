# Generated by Django 3.0.5 on 2020-04-30 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('_id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=20)),
            ],
        ),
    ]
