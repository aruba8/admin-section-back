from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=300, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
