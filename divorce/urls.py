"""form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from divorce import views

admin.site.site_header = "Vibhor Anand"
admin.site.site_title = "Welcome to the Portal "


# from divorce.views import 
urlpatterns = [
    path('', views.form_1, name='form_1'),
    # path('form_2', views.form_2, name='form_2'),
    # path('form_3', views.form_3, name='form_3'),
]
