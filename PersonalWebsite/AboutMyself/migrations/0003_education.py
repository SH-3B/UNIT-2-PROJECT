# Generated by Django 5.1.3 on 2024-11-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutMyself', '0002_remove_interest_title_interest_image_interest_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uni_name', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
