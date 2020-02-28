# Generated by Django 3.0 on 2020-02-28 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('recipe_title', models.CharField(max_length=100)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField(help_text='Write the instructions of your recipe')),
                ('description', models.TextField(help_text='Write the desciption of your recipe')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Page')),
            ],
        ),
    ]
