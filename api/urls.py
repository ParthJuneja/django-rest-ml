from django.urls import path
from . import views

urlpatterns = [
    # path('', views.getData, name="get-data"),
    path(r'^result/$', views.getPred, name="get-pred"),

]
