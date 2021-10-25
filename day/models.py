from django.db import models
from django.utils import timezone

class check_list(models.Model):
    id = models.BigAutoField(primary_key=True)
    creation_date = models.DateField(default=timezone.now)
    is_completed = models.BooleanField(default=False)
    todo_content = models.CharField(max_length=200)
    is_Pin = models.BooleanField(default=True)


    def publish(self):
        self.creation_date = timezone.now()
        self.save()
    def __str__(self):
        return self.todo_content
