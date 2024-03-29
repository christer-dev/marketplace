from django.db import models
from users.models import CustomUser
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

PRODUCT_TYPE_CHOCIES = [('Other', 'Other'),
                    ('Food', 'Food'),
                    ('Apparel', 'Apparel'),
                    ('Outdoors', 'Outdoors'),
                    ('Tech', 'Tech'),
                    ('Memes', 'Memes')]

AVAILABILITY_CHOICES = [('Available', 'Available'),
                        ('Unavailable', 'Unavailable')]

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(1)], null = True, default=0.00)
    productType = models.CharField(max_length = 30, choices = PRODUCT_TYPE_CHOCIES, default='Other')
    description = models.TextField(max_length=1000, blank=True, null = True, default="User hasn't described the product yet.")
    added = models.DateTimeField(auto_now_add=True, auto_now=False)
    seller = models.ForeignKey(CustomUser, on_delete = models.CASCADE, blank=True, null = True)
    picture = models.ImageField(blank=True, null=True, default='defaultProductImage.png', upload_to='products_images')
    averageRating = models.FloatField(default=0)
    availability = models.CharField(max_length = 30, blank=True, null = True, choices = AVAILABILITY_CHOICES, default='Available')
    quantity = models.PositiveIntegerField(default=0)
    users_wishlist = models.ManyToManyField(CustomUser, related_name ="users_wishlist", blank=True)

    def __str__(self):
        return self.name
    
    
    def clean(self):
        if self.quantity < 0:
            raise ValidationError("Quantity must be a positive integer.")
        if self.price < 1:
            raise ValidationError("Price must be a greater than 0.")
    
    def average_rating(self):
        return self.averageRating
    
    def availability_check(self):
        if self.quantity <= 0:
            self.availability = 'Unavailable'
        else:
            self.availability = 'Available'
        self.save()
        print(f"availability_check called for product {self.name}, quantity={self.quantity}, availability={self.availability}")

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0)
    comment = models.TextField(max_length=1000)

    class Meta:
        ordering = ['date_added']

    

# Create your models here.
