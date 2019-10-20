"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.golds,name="golds"),
    path('golds_tz/', views.golds_tz,name="golds_tz"),
    path('golds_gd/', views.golds_gd,name="golds_gd"),
    path('golds_fx/', views.golds_fx,name="golds_fx"),
    path('golds_d/<int:golds_id>', views.golds_d,name="golds_d"),
]
