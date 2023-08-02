from django.db import models

# Create your models here.
'''
 Interact with the database in some way
 It translate how our data is going to look from python code to whatever code in which the database understant

'''
class Book(models.Model):
    title=models.CharField(max_length=100)
    number_of_pages=models.IntegerField()
    publish_date=models.DateField()
    quantity=models.IntegerField()

    def __str__(self):
        return self.title

# /books/list

"""
Creating the model is not enough we actually need to do is to some how migrate the code into sql code
Migration: Interperating model and creating sql code
"""