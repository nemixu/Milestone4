from django.urls import path
from . import views


urlpatterns = [
    path(r'^$', views.search_view, name='search'),

]
