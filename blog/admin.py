from django.contrib import admin
from .models import Autor, Category, Post
# Register your models here.
admin.site.register(Autor)
admin.site.register(Category)
admin.site.register(Post)
