# Generated by Django 3.2.3 on 2021-06-17 09:10

from django.db import migrations, models
import siteapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0005_theme_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_img', models.ImageField(upload_to=siteapp.models.file_path)),
                ('text', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='type_new',
            field=models.CharField(choices=[('main', 'новина'), ('achive', 'досягнення')], default='', max_length=50),
        ),
    ]