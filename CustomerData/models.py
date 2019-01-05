#Customer model

#Django
from django.db import models

class Customer(models.Model):
    #Customer model

    first_Name = models.CharField(max_length=30)
    last_Name = models.CharField(max_length=30)
    
    streetAdd = models.CharField(max_length=60)
    
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=10)

    zipNumber = models.CharField(max_length=10)

    def __str__(self):
        return str(self.pk) + ': ' + self.first_Name + ' ' + self.last_Name
