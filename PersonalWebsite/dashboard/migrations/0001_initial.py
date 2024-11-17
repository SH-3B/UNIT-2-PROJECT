# Generated by Django 5.1.3 on 2024-11-14 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uni_name', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('graduation_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quote', models.TextField(blank=True, default='Not provided')),
                ('why_chose', models.TextField()),
                ('meaning', models.TextField()),
                ('image', models.ImageField(upload_to='interest_images/')),
                ('category', models.CharField(blank=True, choices=[('city', 'Favorite City'), ('drink', 'Favorite Drink'), ('quote', 'Favorite Quote')], default='city', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]