"""
URL configuration for docs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import (
    accordion,
    alert,
    alert_dialog,
    badge,
    button,
    card,
    checkbox,
    command,
    dialog,
    installation,
    introduction,
)

urlpatterns = [
    path("", introduction, name="introduction"),
    path("introduction/", introduction, name="introduction"),
    path("installation/", installation, name="installation"),
    path("accordion/", accordion, name="accordion"),
    path("alert/", alert, name="alert"),
    path("alert-dialog/", alert_dialog, name="alert_dialog"),
    path("badge/", badge, name="badge"),
    path("button/", button, name="button"),
    path("card/", card, name="card"),
    path("checkbox/", checkbox, name="checkbox"),
    path("command/", command, name="command"),
    path("dialog/", dialog, name="dialog"),
]
