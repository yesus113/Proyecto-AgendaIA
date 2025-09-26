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
    
class contact(models.Model):
    name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    mail = models.TextField(max_length=50)
    phone = models.CharField(max_length=15)
    addres = models.TextField(max_length=130)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class event(models.Model):
    title = models.TextField(max_length=50)
    date = models.DateField()
    deadline = models.DateTimeField()
    location = models.TextField(max_length=155)
    hour = models.TimeField()
    description = models.TextField()
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fk_alert = models.ForeignKey("alert", on_delete=models.CASCADE)
    
    
class alert(models.Model):
    date = models.DateField()
    time = models.TimeField()
    fk_event = models.ForeignKey(event, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    
    