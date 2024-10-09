from django.db import models

# Create your models here.
class transaction(models.Model):
    Book_title = models.CharField(max_length=100)
    Member_name = models.CharField(max_length=100)
    Issue_date = models.DateField()
    Return_date = models.DateField()
    Rental_fee = models.IntegerField()

    def __str__(self):
        return self.Book_title
