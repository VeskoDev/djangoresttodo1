from rest_framework.routers import DefaultRouter  

from .views import MovieViewSet

router = DefaultRouter()
router.register('movie', MovieViewSet, basename='prodcuts')


print(router.urls)
urlpatterns = router.urls