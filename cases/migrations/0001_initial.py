# Generated by Django 4.1.1 on 2023-05-08 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField(default='', null=True)),
                ('file01', models.FileField(upload_to='media/files/')),
                ('file02', models.FileField(upload_to='media/files/')),
                ('file03', models.FileField(upload_to='media/files/')),
                ('file04', models.FileField(upload_to='media/files/')),
                ('file05', models.FileField(upload_to='media/files/')),
                ('file06', models.FileField(upload_to='media/files/')),
                ('file07', models.FileField(upload_to='media/files/')),
                ('file08', models.FileField(upload_to='media/files/')),
                ('file09', models.FileField(upload_to='media/files/')),
                ('file10', models.FileField(upload_to='media/files/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
