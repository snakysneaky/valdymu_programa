from django.shortcuts import render

from .models import Task
def management_detail_view(request):
    obj = Task.objects.get(id=1)
    context = {
        'title': obj.title,
        'comments': obj.comments,
    }
    return render(request, "project/detail.html", {})