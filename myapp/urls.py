from django.urls import path
from . import views


app_name = 'shorten_url'
urlpatterns = [
    path('', views.mainview, name= 'main'),
    path('create/', views.createview, name = 'create'),
    path('<int:url_id>', views.updateview),
    path('<int:url_id>/update_main', views.updatemain, name = 'update_main'),
    path('<int:url_id>/update_shorten', views.updateshorten, name = 'update_shorten'),
]