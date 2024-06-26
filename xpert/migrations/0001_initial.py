# Generated by Django 5.0.4 on 2024-04-22 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_picture', models.ImageField(default='project.jpg', upload_to='project_pictures/')),
                ('project_name', models.CharField(max_length=150)),
                ('project_description', models.CharField(blank=True, max_length=500)),
                ('project_status', models.CharField(choices=[('Completed', 'Completed'), ('Ongoing', 'Ongoing')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_rating', models.CharField(choices=[('1', '1 Star'), ('2', '2 Stars'), ('3', '3 Stars'), ('4', '4 Stars'), ('5', '5 Stars')], max_length=1)),
                ('review', models.CharField(max_length=500)),
                ('review_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=150)),
                ('service_description', models.CharField(max_length=500)),
            ],
        ),
    ]
