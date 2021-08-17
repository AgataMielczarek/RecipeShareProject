from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.log, name='log'),
    path('logout', views.logoutuser, name='logout'),
    path('create', views.create, name='create'),
    path('<int:reId>', views.detail, name='detail'),
    path('my', views.my, name='my'),
    path('my/<int:reId>', views.edit, name='edit'),
    path('delete/<int:reId>', views.deleteRec, name='delete'),
    path('search', views.search, name='search'),
    path('cuisine/<str:cuisineKey>', views.display_cuisine, name='display_cuisine'),
    path('level/<str:levelKey>', views.display_level, name='display_level'),

]
