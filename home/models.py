from django.db import models

# Create your models here.
class Enquiries(models.Model):
    email = models.EmailField(max_length=254)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + self.email