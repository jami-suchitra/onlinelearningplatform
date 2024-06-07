from django.db import models

class Canvas(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name