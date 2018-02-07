"""codecaracas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', views.home, name='home'),
    path('Blog/', views.blog, name='blog'),
    path('Blog/<int:page>', views.blog_next, name='blog_next'),
    path('Categorias/<str:name_category>/', views.post_by_category, name='category'),
    path('Categorias/<str:name_category>/<int:page>', views.post_by_category_next, name='category_next'),
    path('Autores/<str:name_autor>/', views.post_by_autor, name='autor'),
    path('Autores/<str:name_autor>/<int:page>', views.post_by_autor_next, name='autor_next'),
    path('Post/<str:title_post>/', views.single_post, name='single_post')
]
