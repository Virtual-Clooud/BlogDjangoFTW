from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    altura = models.DecimalField(default = 0.00, max_digits=5,decimal_places=2)
    # Outros campos personalizados que você queira adicionar

    def __str__(self):
        return self.username
    
