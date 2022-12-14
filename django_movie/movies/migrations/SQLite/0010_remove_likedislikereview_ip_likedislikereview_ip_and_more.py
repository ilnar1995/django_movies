# Generated by Django 4.0.6 on 2022-08-12 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_movie_tagline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likedislikereview',
            name='ip',
        ),
        migrations.AddField(
            model_name='likedislikereview',
            name='ip',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='likedislikereview', to='movies.ip_addres', verbose_name='IP адрес'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='ratingmovie',
            name='ip',
        ),
        migrations.AddField(
            model_name='ratingmovie',
            name='ip',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ratingmovie', to='movies.ip_addres', verbose_name='IP адрес'),
            preserve_default=False,
        ),
    ]
