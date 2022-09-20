from django.contrib import admin
from .models import *
#Register your models here.

admin.site.register(Category)
admin.site.register(IP_addres)
admin.site.register(Actor)
admin.site.register(Review)
admin.site.register(Quality)
admin.site.register(Translation)
admin.site.register(Movie)
admin.site.register(RatingMovie)
admin.site.register(Genre)
admin.site.register(LikeDislikeReview)

admin.site.site_title = "Django Movies"
admin.site.site_header = "Django Movies"