from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    color = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.color


class ShoeGender(models.Model):
    name = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Shoe(models.Model):
    model = models.CharField(max_length=200)
    gender = models.ForeignKey(ShoeGender, on_delete=models.CASCADE, null=True)
    size = models.DecimalField(max_digits=3, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=200)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model
