from django.db import models

# Create your models here.
class numbers(models.Model):
    fnum = models.IntegerField
    
    
    def _int_(self):
        return self.fnum
