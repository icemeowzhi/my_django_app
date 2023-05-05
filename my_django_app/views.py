from django.shortcuts import render


def hello_world_page(request):
    context = {"text": ["Hello World! You know that.","<a href='../admin'>to admin</a>"]}
    return render(request, "hello_world.html", context)
