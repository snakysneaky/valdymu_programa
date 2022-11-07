from django.db import models

# Create your models here.
class Project(models.Model):
    title       = models.CharField(max_length=200)
    start_date  = models.DateField()
    end_date    = models.DateField()
    customer    = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    manager     = models.ForeignKey('self', on_delete=models.CASCADE, limit_choices_to={'manager_id': True},)
    employee    = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
    tasks       = models.ForeignKey('Task', on_delete=models.SET_NULL, null=True)
    bills       = models.ForeignKey('Account', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Customer(models.Model):
    first_name  = models.CharField(max_length=120)
    last_name   = models.CharField(max_length=120)
    company     = models.CharField(max_length=200)
    contacts    = models.TextField()

class Employee(models.Model):
    first_name  = models.CharField(max_length=120)
    last_name   = models.CharField(max_length=120)
    position    = models.CharField(max_length=120)

class Task(models.Model):
    title       = models.CharField(max_length=200)
    comments    = models.TextField(blank=True, null=True)

    STATUS = (("n", "NEW"), ("d", "Done"), ("o", "On going"), ("p", "Postponed"), ("c", "Canceled"),)

    status = models.CharField(max_length=1, choices=STATUS, help_text="status")

class Account(models.Model):
    the_date_of_issue = models.DateField()
    amount            = models.DecimalField(decimal_places=2, max_digits=10000)
