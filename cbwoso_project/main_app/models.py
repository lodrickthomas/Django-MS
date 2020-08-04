from django.db import models

# Create your models here.


class Position(models.Model):
    TITLES = (
        ('', 'Choose...'),
        ('Eng.', 'Eng.'),
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
    )
    title = models.CharField(max_length=30, choices=TITLES, default='Choose...')

    def __str__(self):
        return self.title


class Employee(models.Model):

    position= models.ForeignKey(Position, on_delete=models.CASCADE)
    first_name= models.CharField(max_length=30, default=None)
    last_name= models.CharField(max_length=30, default=None)
    registration_number= models.CharField(max_length=30, default=None)
    phone_number= models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.first_name

    #class Meta:
     #   ordering = ['headline']
