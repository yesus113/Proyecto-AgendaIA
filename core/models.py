from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    state = models.CharField(
        max_length=20,
        choices=[
            ("sin empezar", "Sin Empezar"),
            ("en curso", "En Curso"),
            ("listo", "Listo"),
        ],
        default="sin empezar")
    
    deadline = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(datetime.now())
    fk_user_id = models.ForeignKey(  User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    
    