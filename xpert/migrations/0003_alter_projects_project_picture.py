# Generated by Django 5.0.4 on 2024-04-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xpert', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_picture',
            field=models.ImageField(default='project.jpg', upload_to='project_pictures'),
        ),
    ]
