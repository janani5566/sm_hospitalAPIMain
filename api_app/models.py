from django.db import models

# Create your models here.

class login(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    class Meta:
        db_table = 'login_tbl'

    def __str__ (self):
       return self.name


class Secondary(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    class Meta:
        db_table = 'Secondary_tbl'

    def __str__ (self):
       return self.name