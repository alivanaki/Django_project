from django.urls import path
from . import views


app_name = 'shorten_url'
urlpatterns = [
    path('', views.MainPageView.as_view(), name= 'main'),
    path('create/', views.CreateURLView.as_view(), name = 'create'),
    path('<pk>', views.URLDetailView.as_view(), name='detail'),
    path('<int:url_id>/update_main', views.updatemain, name = 'update_main'),
    path('<int:url_id>/update_shorten', views.updateshorten, name = 'update_shorten'),
]