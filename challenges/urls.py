from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    # path("january", views.january),
    # path('february', views.february),
    path('<month>', views.month_function)
]
