# Generated by Django 2.2 on 2019-04-26 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('genre_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('imdb_rating', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('rt_rating', models.IntegerField(null=True)),
                ('description', models.TextField()),
                ('movie_id', models.CharField(max_length=60)),
                ('thumbnail_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showvies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showvies.Genre')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showvies.Movie')),
            ],
        ),
    ]
