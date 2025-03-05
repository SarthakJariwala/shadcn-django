from django.shortcuts import render


def introduction(request):
    return render(request, "introduction.html")


def installation(request):
    return render(request, "installation.html")


def button(request):
    return render(request, "button.html")
