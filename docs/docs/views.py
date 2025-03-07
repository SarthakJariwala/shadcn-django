from django.shortcuts import render


def introduction(request):
    return render(request, "introduction.html")


def installation(request):
    return render(request, "installation.html")


def accordion(request):
    return render(request, "accordion.html")


def alert(request):
    return render(request, "alert.html")


def alert_dialog(request):
    return render(request, "alert_dialog.html")


def badge(request):
    return render(request, "badge.html")


def button(request):
    return render(request, "button.html")


def card(request):
    return render(request, "card.html")


def checkbox(request):
    return render(request, "checkbox.html")


def command(request):
    return render(request, "command.html")


def dialog(request):
    return render(request, "dialog.html")


def dropdown_menu(request):
    return render(request, "dropdown_menu.html")


def form(request):
    return render(request, "form.html")


def input(request):
    return render(request, "input.html")


def label(request):
    return render(request, "label.html")


def progress(request):
    return render(request, "progress.html")


def table(request):
    return render(request, "table.html")


def tabs(request):
    return render(request, "tabs.html")


def textarea(request):
    return render(request, "textarea.html")


def toast(request):
    return render(request, "toast.html")
