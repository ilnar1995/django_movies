# Generated by Django 4.0.6 on 2022-07-31 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='IP_addres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Слоган')),
                ('title', models.CharField(max_length=200, verbose_name='Название в оригинале')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Постер')),
                ('year', models.PositiveSmallIntegerField(default=2022, verbose_name='Дата выхода')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('link', models.URLField(verbose_name='Ссылка на видео')),
                ('draft', models.BooleanField(default=False, verbose_name='Скрытость')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movies.actor', verbose_name='актеры')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category', verbose_name='Категория')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movies.actor', verbose_name='режиссер')),
                ('genre', models.ManyToManyField(to='movies.genre', verbose_name='жанры')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.movie', verbose_name='фильм')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='movies.review', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='RatingMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField(choices=[(1, 'like'), (-1, 'dislike')], verbose_name='Голос')),
                ('ip', models.ManyToManyField(related_name='ratingmovie', to='movies.ip_addres', verbose_name='IP адрес')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movies.movie', verbose_name='фильм')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='quality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.quality', verbose_name='Качество'),
        ),
        migrations.AddField(
            model_name='movie',
            name='translation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.translation', verbose_name='Перевод'),
        ),
        migrations.CreateModel(
            name='LikeDislikeReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField(choices=[(1, 'like'), (-1, 'dislike')], verbose_name='Голос')),
                ('Review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.review', verbose_name='звезда')),
                ('ip', models.ManyToManyField(related_name='likedislikereview', to='movies.ip_addres', verbose_name='IP адрес')),
            ],
        ),
    ]
