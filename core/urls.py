from core.views import announcements
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/announcements.html', views.announcements, name='announcements'),
    path('home/policies.html', views.policies, name='policies'),
    path('home/terms-conditions.html', views.terms_conditions, name='terms-conditions')
]
