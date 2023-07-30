from rest_framework.routers import SimpleRouter
from .views import ShortenerView

app_name = 'shorten_url'
router = SimpleRouter()
router.register(r'', ShortenerView, basename='url')
urlpatterns = router.urls
