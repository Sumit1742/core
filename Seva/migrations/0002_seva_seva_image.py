# Generated by Django 5.1.5 on 2025-03-25 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seva', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seva',
            name='Seva_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='Seva/'),
        ),
    ]
