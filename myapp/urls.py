from django.urls import path
from .views import MainPageView, CreateURLView, URLDetailView


app_name = 'shorten_url'
urlpatterns = [
    path('', MainPageView.as_view(), name= 'main'),
    path('create/', CreateURLView.as_view(), name = 'create'),
    path('<pk>', URLDetailView.as_view(), name='detail'),
    #path('<int:url_id>/update_main', views.updatemain, name = 'update_main'),
    #path('<int:url_id>/update_shorten', views.updateshorten, name = 'update_shorten'),
]