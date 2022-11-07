from django.http import HttpResponse
from django.shortcuts import render

def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World!</h1>")

def about_view(*args, **kwargs):
    my_context = {
        "title": "this is about the office"
        "this_is_true": True,
        "my_number": 123,
        "my_list": [3131, 6565, 7574],
        "my_html": "<h1>Hello World</h1>"
    }
    return render(request, "about.html", my_context)