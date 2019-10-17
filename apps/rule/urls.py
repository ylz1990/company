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
    path('', views.rule, name="rule"),
    path('ywgz/', views.ywgz, name="ywgz"),
    path('qsjs/', views.qsjs, name="qsjs"),
    path('jgdj/', views.jgdj, name="jgdj"),
    path('fxqzl/', views.fxqzl, name="fxqzl"),
    path('rule_d/<int:rule_id>', views.rule_d, name="rule_d"),
]
