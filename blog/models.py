from django.db import models


class Autor(models.Model):
    Autor_User = models.CharField(max_length=30, unique=True)
    Autor_Name = models.CharField(max_length=30)
    Autor_Mail = models.CharField(max_length=30, unique=True)
    Autor_Phone = models.CharField(max_length=20, unique=True)
    Autor_Password = models.CharField(max_length=20)
    Autor_Avatar = 1

    def __unicode__(self):
        return self.Autor_Name


class Category(models.Model):
    Category_Name = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.Category_Name


class Post(models.Model):
    Post_Title = models.CharField(max_length=50, unique=True)
    Post_Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    Post_Content = models.TextField()
    Post_Creation_Date = models.DateField()
    Post_Autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    Post_About = models.CharField(max_length=200)
    Post_About_Short = models.CharField(max_length=100)
    Post_Cover_Image = 1

    def __unicode__(self):
        return self.Post_Title
