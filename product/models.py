from django.db import models


CATEGORY_CHOICES = (
    ('featured','FEATURED'),
    ('recommended', 'RECOMMENDED'),
    ('sports','SPORTS'),
    ('groccery','GROCERY'),
    ('clothing','CLOTHING'),
    ('spices','SPICES'),
    ('fruits','FRUITS'),
    ('vegitables','VEGITABLES'),
    
)

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    image=models.CharField(max_length=500)
    category=models.CharField(max_length=50, choices=CATEGORY_CHOICES)


