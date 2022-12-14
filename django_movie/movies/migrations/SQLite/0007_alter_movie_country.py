# Generated by Django 4.0.6 on 2022-08-09 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_alter_movie_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(choices=[('США', 'США'), ('Россия', 'Россия'), ('Австралия', 'Австралия'), ('Австрия', 'Австрия'), ('Албания', 'Албания'), ('Андорра', 'Андорра'), ('Аргентина', 'Аргентина'), ('Афганистан', 'Афганистан'), ('Беларусь', 'Беларусь'), ('Бельгия', 'Бельгия'), ('Болгария', 'Болгария'), ('Бразилия', 'Бразилия'), ('Великобритания', 'Великобритания'), ('Венгрия', 'Венгрия'), ('Вьетнам', 'Вьетнам'), ('Гана', 'Гана'), ('Германия', 'Германия'), ('Германия (ФРГ)', 'Германия (ФРГ)'), ('Гонконг', 'Гонконг'), ('Греция', 'Греция'), ('Грузия', 'Грузия'), ('Дания', 'Дания'), ('Израиль', 'Израиль'), ('Индия', 'Индия'), ('Индонезия', 'Индонезия'), ('Иордания', 'Иордания'), ('Иран', 'Иран'), ('Ирландия', 'Ирландия'), ('Исландия', 'Исландия'), ('Испания', 'Испания'), ('Италия', 'Италия'), ('Казахстан', 'Казахстан'), ('Камбоджа', 'Камбоджа'), ('Канада', 'Канада'), ('Катар', 'Катар'), ('Кения', 'Кения'), ('Китай', 'Китай'), ('Колумбия', 'Колумбия'), ('Корея Северная', 'Корея Северная'), ('Корея Южная', 'Корея Южная'), ('Кыргызстан', 'Кыргызстан'), ('Латвия', 'Латвия'), ('Ливан', 'Ливан'), ('Литва', 'Литва'), ('Люксембург', 'Люксембург'), ('Македония', 'Македония'), ('Малайзия', 'Малайзия'), ('Мальта', 'Мальта'), ('Марокко', 'Марокко'), ('Мексика', 'Мексика'), ('Нидерланды', 'Нидерланды'), ('НоваяЗеландия', 'НоваяЗеландия'), ('Норвегия', 'Норвегия'), ('ОАЭ', 'ОАЭ'), ('Пакистан', 'Пакистан'), ('Парагвай', 'Парагвай'), ('Перу', 'Перу'), ('Польша', 'Польша'), ('Португалия', 'Португалия'), ('Пуэрто Рико', 'Пуэрто Рико'), ('Румыния', 'Румыния'), ('СССР', 'СССР'), ('Сербия', 'Сербия'), ('Сингапур', 'Сингапур'), ('Словакия', 'Словакия'), ('Таиланд', 'Таиланд'), ('Тайвань', 'Тайвань'), ('Турция', 'Турция'), ('Узбекистан', 'Узбекистан'), ('Украина', 'Украина'), ('Уругвай', 'Уругвай'), ('Фарерскиеострова', 'Фарерскиеострова'), ('Филиппины', 'Филиппины'), ('Финляндия', 'Финляндия'), ('Франция', 'Франция'), ('Хорватия', 'Хорватия'), ('Чехия', 'Чехия'), ('Чехословакия', 'Чехословакия'), ('Чили', 'Чили'), ('Швейцария', 'Швейцария'), ('Швеция', 'Швеция'), ('Эстония', 'Эстония'), ('ЮАР', 'ЮАР'), ('Япония', 'Япония')], max_length=30, verbose_name='Страна'),
        ),
    ]
