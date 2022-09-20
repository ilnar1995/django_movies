from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.db.models import Count, Sum, Q, F, Func
from django.urls import reverse
from django.conf import settings

countrys = (
        ("США", "США"), ("Россия", "Россия"), ("Австралия", "Австралия"), ("Австрия", "Австрия"),
        ("Албания", "Албания"),
        ("Андорра", "Андорра"), ("Аргентина", "Аргентина"), ("Афганистан", "Афганистан"), ("Беларусь", "Беларусь"),
        ("Бельгия", "Бельгия"), ("Болгария", "Болгария"), ("Бразилия", "Бразилия"),
        ("Великобритания", "Великобритания"),
        ("Венгрия", "Венгрия"), ("Вьетнам", "Вьетнам"), ("Гана", "Гана"), ("Германия", "Германия"),
        ("Германия (ФРГ)", "Германия (ФРГ)"),
        ("Гонконг", "Гонконг"), ("Греция", "Греция"), ("Грузия", "Грузия"), ("Дания", "Дания"), ("Израиль", "Израиль"),
        ("Индия", "Индия"),
        ("Индонезия", "Индонезия"), ("Иордания", "Иордания"), ("Иран", "Иран"), ("Ирландия", "Ирландия"),
        ("Исландия", "Исландия"),
        ("Испания", "Испания"), ("Италия", "Италия"), ("Казахстан", "Казахстан"), ("Камбоджа", "Камбоджа"),
        ("Канада", "Канада"),
        ("Катар", "Катар"), ("Кения", "Кения"), ("Китай", "Китай"), ("Колумбия", "Колумбия"),
        ("Корея Северная", "Корея Северная"),
        ("Корея Южная", "Корея Южная"), ("Кыргызстан", "Кыргызстан"), ("Латвия", "Латвия"), ("Ливан", "Ливан"),
        ("Литва", "Литва"),
        ("Люксембург", "Люксембург"), ("Македония", "Македония"), ("Малайзия", "Малайзия"), ("Мальта", "Мальта"),
        ("Марокко", "Марокко"),
        ("Мексика", "Мексика"), ("Нидерланды", "Нидерланды"), ("НоваяЗеландия", "НоваяЗеландия"),
        ("Норвегия", "Норвегия"), ("ОАЭ", "ОАЭ"),
        ("Пакистан", "Пакистан"), ("Парагвай", "Парагвай"), ("Перу", "Перу"), ("Польша", "Польша"),
        ("Португалия", "Португалия"),
        ("Пуэрто Рико", "Пуэрто Рико"), ("Румыния", "Румыния"), ("СССР", "СССР"), ("Сербия", "Сербия"),
        ("Сингапур", "Сингапур"),
        ("Словакия", "Словакия"), ("Таиланд", "Таиланд"), ("Тайвань", "Тайвань"), ("Турция", "Турция"),
        ("Узбекистан", "Узбекистан"),
        ("Украина", "Украина"), ("Уругвай", "Уругвай"), ("Фарерскиеострова", "Фарерскиеострова"),
        ("Филиппины", "Филиппины"), ("Финляндия", "Финляндия"),
        ("Франция", "Франция"), ("Хорватия", "Хорватия"), ("Чехия", "Чехия"), ("Чехословакия", "Чехословакия"),
        ("Чили", "Чили"),
        ("Швейцария", "Швейцария"), ("Швеция", "Швеция"), ("Эстония", "Эстония"), ("ЮАР", "ЮАР"), ("Япония", "Япония")
    )

class Actor(models.Model):
    """Актеры и режиссеры"""
    name = models.CharField("Имя", max_length=100)

    def __str__(self):
        return self.name

    class Meta: #для админ панели
        verbose_name = "Актеры"
        verbose_name_plural = "Актеры"

class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self, categ = 'film'):
        if categ:
            return reverse('category', kwargs={'cat_slug': categ, 'genre_slug': self.url})
        else:
            return reverse('category', args=[self.url])  # в vi было kwargs={'cat_slug': self.slug}

    class Meta: #для админ панели
        verbose_name = "Жанры"
        verbose_name_plural = "Жанры"

class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[self.url])  # в видео было kwargs={'cat_slug': self.slug}

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Quality(models.Model):
    """Качество"""
    title = models.CharField("Название", max_length=100)

    def __str__(self):
        return self.title

    class Meta: #для админ панели
        verbose_name = "Качество"
        verbose_name_plural = "Качество"

class Translation(models.Model):
    """Перевод"""
    title = models.CharField("Название", max_length=100)

    def __str__(self):
        return self.title

    class Meta: #для админ панели
        verbose_name = "Перевод"
        verbose_name_plural = "Перевод"

class IP_addres(models.Model):
    """"ip адрес клиента"""
    ip = models.CharField("IP адрес", max_length=15)
    def __str__(self):
        return self.ip

class Movie(models.Model):
    """фильмы"""
    name = models.CharField("Имя", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='', blank=True, null=True)
    title = models.CharField("Название в оригинале", max_length=200)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=130, unique=True)
    poster = models.ImageField("Постер", upload_to="poster/%Y/%m/%d/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2022)
    country = models.CharField("Страна", max_length=30, choices=countrys)
    genre = models.ManyToManyField(Genre, verbose_name="жанры")
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    link = models.URLField('Ссылка на видео', max_length=200)
    imdb = models.FloatField("IMDB", validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True, null=True)
    kr = models.FloatField("КР", validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], blank=True, null=True)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    quality = models.ForeignKey(
        Quality, verbose_name="Качество", on_delete=models.SET_NULL, null=True
    )
    translation = models.ForeignKey(
        Translation, verbose_name="Перевод", on_delete=models.SET_NULL, null=True
    )
    draft = models.BooleanField("Скрытость", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return reverse("movie_detail", kwargs={"movie_slug": self.url})
        return '/movies/{}/'.format(self.url)

    class Meta: #для админ панели
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    # @property
    # def rating_movie_method(self):
    #     return self.ratings.aggregate(like=Count('vote', filter=Q(vote=1)), dislike=Count('vote', filter=Q(vote=-1)))

class RatingMovie(models.Model):
    """рейтинг"""
    LIKE = 1
    DISLIKE = -1
    VOTES = (
        (LIKE, "like"),
        (DISLIKE, "dislike")
    )
    vote = models.SmallIntegerField(verbose_name="Голос", choices=VOTES)
    ip = models.ForeignKey(IP_addres, verbose_name="IP адрес", related_name='ratingmovie', on_delete=models.CASCADE)
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        verbose_name="фильм",
        related_name="ratings"
    )

class Review(models.Model):
    """Отзывы"""
    email = models.EmailField("Почта", blank=True, null=True)
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
    'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name="children"
    )
    movie = models.ForeignKey(
        Movie, verbose_name="фильм", on_delete=models.CASCADE, related_name="reviews"
    )
    time_create = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class LikeDislikeReview(models.Model):
    """Лайк и дизлайк отзыва"""
    LIKE = 1
    DISLIKE = -1
    VOTES = (
        (LIKE, "like"),
        (DISLIKE, "dislike")
    )
    vote = models.SmallIntegerField(verbose_name="Голос", choices=VOTES)
    ip = models.ForeignKey(IP_addres, verbose_name="IP адрес", related_name='likedislikereview', on_delete=models.CASCADE)
    Review = models.ForeignKey(Review, on_delete=models.CASCADE, verbose_name="звезда", related_name='likedislikereview')
