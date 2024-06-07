from django.db import models
from django.contrib.auth.models import User

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='enrolled_classes')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.name