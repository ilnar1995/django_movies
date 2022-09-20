# Generated by Django 4.0.6 on 2022-08-02 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'verbose_name': 'Актеры', 'verbose_name_plural': 'Актеры'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанры', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='quality',
            options={'verbose_name': 'Качество', 'verbose_name_plural': 'Качество'},
        ),
        migrations.AlterModelOptions(
            name='translation',
            options={'verbose_name': 'Перевод', 'verbose_name_plural': 'Перевод'},
        ),
        migrations.AddField(
            model_name='review',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='poster/%Y/%m/%d/', verbose_name='Постер'),
        ),
    ]
