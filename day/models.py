from django.db import models


class check_list(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_completed = models.BooleanField(default=False)
    todo_content = models.CharField(max_length = 200)
    is_Pin = models.BooleanField(default=True)
