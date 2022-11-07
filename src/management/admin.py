from django.contrib import admin
from .models import Project, Customer, Employee, Task, Account

admin.site.register(Project)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(Account)

