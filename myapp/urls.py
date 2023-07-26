from django.urls import path
from .views import MainPageView, CreateURLView, URLDetailView, DeleteURLView, UpdateURLView


app_name = 'shorten_url'
urlpatterns = [
    path('', MainPageView.as_view(), name= 'main'),
    path('create/', CreateURLView.as_view(), name = 'create'),
    path('<pk>', URLDetailView.as_view(), name='detail'),
    path('<pk>/delete/', DeleteURLView.as_view(), name='delete'),
    path('<pk>/update', UpdateURLView.as_view(), name = 'update'),
]
