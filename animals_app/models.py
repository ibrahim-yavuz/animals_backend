from django.db import models

class Animal(models.Model):
    animal_name = models.CharField(max_length=60)
    about_animal = models.TextField()
    animal_image_src = models.TextField()

    def __str__(self):
        return self.animal_name
