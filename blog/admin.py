from django.contrib import admin
from .models import Post        #это, походу, импортирован класс Post из models.py

admin.site.register(Post)       #регистрирование модели, чтобы она стала доступна в админке
