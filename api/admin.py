from django.contrib import admin
from .models import Movie, Comment

# Register your models here.

models = [Movie, Comment]
admin.site.register(models)
