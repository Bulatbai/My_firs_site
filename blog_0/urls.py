from django.urls import path
from . import views
urlpatterns = [
    path('', views.Logic, name='page_11'),
    path('res/', views.Logik, name='Page12'),

]
