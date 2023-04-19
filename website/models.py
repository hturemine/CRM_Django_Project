from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    
    def __str__(self):
        return(f"{self.first_Name} {self.last_Name}")
