from django.db import models
from picklefield.fields import PickledObjectField

class Client(models.Model):  
    name = models.CharField(max_length=30, null=True)
    guardian = models.CharField(max_length=30, null=True)
    cnic = models.CharField(primary_key=True, max_length=15, unique=True)
    contact = models.CharField(max_length=12, null=True)
    status = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.cnic + " - " + self.name

class Property(models.Model):  
    plot = models.CharField(max_length=10, primary_key=True, unique=True)
    size = models.IntegerField(null=True)
    block = models.CharField(max_length=5)
    amount = models.IntegerField()
    category = models.CharField(max_length=12)
    status = models.CharField(max_length=12, null=True)

    def __str__(self):
        return str(self.plot) + " - " + str(self.size) + " - " + self.block + " - " + self.category

class File(models.Model):  
    file = models.CharField(max_length=30, primary_key=True, unique=True)
    agent = models.CharField(max_length=30)
    client = models.ForeignKey(Client, max_length=30, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, max_length=30, on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
    payment = PickledObjectField()

    def __str__(self):
        return self.file