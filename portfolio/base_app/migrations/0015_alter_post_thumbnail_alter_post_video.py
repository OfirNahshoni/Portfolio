# Generated by Django 4.1.6 on 2023-03-12 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0014_alter_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/videos'),
        ),
    ]
