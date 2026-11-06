from django.db import models

class Task(models.Model):
    content = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.content