# Generated by Django 5.1.5 on 2025-03-21 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seva_iocn', models.CharField(max_length=100)),
                ('Seva_title', models.CharField(max_length=100)),
                ('Seva_desc', models.TextField()),
            ],
        ),
    ]
