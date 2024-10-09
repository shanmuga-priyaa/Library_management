from django.db import models

class Book(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=13, unique=True)
    Publisher = models.CharField(max_length=100)
    Page_count = models.IntegerField()
    Available = models.BooleanField()

    def __str__(self):
        return self.Title
