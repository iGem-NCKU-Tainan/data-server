from django.conf.urls import url
from app16 import views

urlpatterns = [
    url(r'^$', views.index)
]
