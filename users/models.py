from django.db import models


class user_data(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=130)
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.username