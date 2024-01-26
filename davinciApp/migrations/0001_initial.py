# Generated by Django 4.2.9 on 2024-01-26 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('blogIdea', models.CharField(blank=True, max_length=200, null=True)),
                ('keywords', models.CharField(blank=True, max_length=300, null=True)),
                ('audience', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'blog',
            },
        ),
    ]