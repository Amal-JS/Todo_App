from django.db import models

# Create your models here.

class Todo(models.Model):
    task_name=models.CharField(max_length=50)
    date=models.DateField()


    class Meta:
        db_table= "Test DB"

    def __str__(self):
        return self.task_name