from rest_framework.routers import DefaultRouter  

from .views import MovieViewSet, TagViewSet

router = DefaultRouter()
router.register('movie', MovieViewSet, basename='prodcuts')
router.register('tags', TagViewSet, basename='tags')


urlpatterns = router.urls