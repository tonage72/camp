# Generated by Django 3.2.11 on 2022-04-08 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_first_name', models.CharField(max_length=20)),
                ('member_last_name', models.CharField(max_length=20)),
            ],
        ),
    ]
