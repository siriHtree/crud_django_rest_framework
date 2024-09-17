from django.db import models

# Create your models here.
"""
Interact with the database in some way.
It translates how our data is going to look from Python code to whatever code in which the database understands.
"""
class Book(models.Model):
    title = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()
    author = models.CharField(max_length=100)  # New field added

    def __str__(self):
        return self.title

# /books/list

"""
Creating the model is not enough; we actually need to do is to somehow migrate the code into SQL code.
Migration: Interpreting model and creating SQL code.
"""