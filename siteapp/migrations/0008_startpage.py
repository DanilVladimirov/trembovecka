# Generated by Django 3.2.3 on 2021-06-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0007_auto_20210617_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
            ],
        ),
    ]
