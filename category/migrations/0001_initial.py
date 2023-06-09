# Generated by Django 4.2.1 on 2023-07-09 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NameCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='NeckExercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercises_number_one', models.TextField()),
                ('exercises_number_two', models.TextField()),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.namecategory')),
            ],
        ),
        migrations.CreateModel(
            name='HandExercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercises_number_one', models.TextField()),
                ('exercises_number_two', models.TextField()),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.namecategory')),
            ],
        ),
        migrations.CreateModel(
            name='EyeExercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercises_number_one', models.TextField()),
                ('exercises_number_two', models.TextField()),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.namecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercises_number_one', models.TextField()),
                ('exercises_number_two', models.TextField()),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.namecategory')),
            ],
        ),
    ]
