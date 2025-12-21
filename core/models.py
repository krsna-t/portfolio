from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
