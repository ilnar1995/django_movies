# Generated by Django 4.0.6 on 2022-08-04 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_ip_addres_movie_alter_likedislikereview_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ip_addres',
            name='movie',
        ),
    ]