from django.db import models

# Create your models here.


class Employee(models.Model):
    eid = models.CharField(max_length=100)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=100)

    def __str__(self):
        return self.ename

    class Meta:
        db_table = "employee"
