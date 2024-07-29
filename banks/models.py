from django.db import models
from django.contrib.auth.models import User

class Bank(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    inst_num = models.CharField(max_length=100)
    swift_code = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Branch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    transit_num = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    capacity = models.PositiveIntegerField()
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
