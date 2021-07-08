# Generated by Django 2.2.6 on 2021-07-07 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TvShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('content_rating', models.CharField(max_length=16)),
                ('description', models.TextField(blank=True)),
                ('poster', models.ImageField(max_length=512, upload_to='posters')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.TimeField()),
                ('type', models.CharField(default='video/mp4', max_length=64)),
                ('hd', models.BooleanField(default=False)),
                ('path', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Subtitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(default='en-us', max_length=8)),
                ('path', models.CharField(max_length=1024)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtitles', to='netflix.Video')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('release_date', models.DateField()),
                ('content_rating', models.CharField(max_length=16)),
                ('description', models.TextField(blank=True)),
                ('poster', models.ImageField(max_length=512, upload_to='posters')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.Video')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('air_date', models.DateField()),
                ('episode_num', models.SmallIntegerField()),
                ('season_num', models.SmallIntegerField()),
                ('description', models.TextField(blank=True)),
                ('tv_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='netflix.TvShow')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netflix.Video')),
            ],
        ),
    ]