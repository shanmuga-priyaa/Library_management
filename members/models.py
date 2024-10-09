from django.db import models

# Create your models here.
class member(models.Model):
    Member_name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Outstanding_debt = models.IntegerField(default=0)

    def __str__(self):
        return self.Member_name