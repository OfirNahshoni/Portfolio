# Generated by Django 4.1.6 on 2023-02-23 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='repo_link',
            field=models.CharField(max_length=150, null=True),
        ),
    ]