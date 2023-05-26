# Generated by Django 4.2.1 on 2023-05-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackExercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hand_rotations', models.CharField(max_length=230)),
                ('pull_ups', models.CharField(max_length=230)),
            ],
        ),
        migrations.CreateModel(
            name='LegExercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warm_up', models.CharField(max_length=230)),
                ('jumping', models.CharField(max_length=230)),
                ('sit_ups', models.CharField(max_length=230)),
            ],
        ),
        migrations.CreateModel(
            name='ProUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_card', models.CharField(max_length=230)),
                ('cvc_card', models.CharField(max_length=230)),
                ('valid_thru', models.CharField(max_length=230)),
                ('name_card', models.CharField(max_length=230)),
            ],
        ),
    ]
