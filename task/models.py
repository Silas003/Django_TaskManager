from django.db import models



class Task(models.Model):
    Title=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Title