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


def combobox(request):
    return render(request, "combobox.html")


def command(request):
    return render(request, "command.html")


def command_dialog(request):
    return render(request, "command_dialog.html")


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


def navigation_menu(request):
    return render(request, "navigation_menu.html")


def popover(request):
    return render(request, "popover.html")


def progress(request):
    return render(request, "progress.html")


def select(request):
    return render(request, "select.html")


def separator(request):
    return render(request, "separator.html")


def sheet(request):
    sides = ["top", "right", "bottom", "left"]
    return render(request, "sheet.html", {"sides": sides})


def table(request):
    return render(request, "table.html")


def tabs(request):
    return render(request, "tabs.html")


def textarea(request):
    return render(request, "textarea.html")


def toast(request):
    return render(request, "toast.html")
