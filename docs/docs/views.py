from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def click(request):
    if request.htmx:
        return render(request, "partials/click.html")
