from django.db import models
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField

class Agent(models.Model):  
    name = models.CharField(max_length=30, null=True)
    guardian = models.CharField(max_length=30, null=True)
    cnic = models.CharField(primary_key=True, max_length=15, unique=True)
    contact = models.CharField(max_length=12, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.cnic + " - " + self.name

class Client(models.Model):  
    name = models.CharField(max_length=30, null=True)
    guardian = models.CharField(max_length=30, null=True)
    cnic = models.CharField(primary_key=True, max_length=15, unique=True)
    contact = models.CharField(max_length=12, null=True)
    status = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.cnic + " - " + self.name

class Property(models.Model):  
    plot = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    size = models.IntegerField()
    block = models.CharField(max_length=5)
    amount = models.IntegerField()
    category = models.CharField(max_length=12)
    status = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.name

class File(models.Model):  
    file = models.CharField(max_length=30, primary_key=True, unique=True)
    agent = models.ForeignKey(Agent, max_length=30, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, max_length=30, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, max_length=30, on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
    payment = ArrayField(
        ArrayField(
            models.CharField(max_length=30, blank=True),
            size=3,
        ),
    )

    def __str__(self):
        return self.file