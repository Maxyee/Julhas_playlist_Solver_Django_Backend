# Generated by Django 2.2 on 2019-05-10 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20190430_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='file',
            field=models.FileField(default='no-video', upload_to=''),
        ),
    ]