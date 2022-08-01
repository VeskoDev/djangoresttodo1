from rest_framework.routers import DefaultRouter  

from .views import MovieViewSet, TagViewSet, TitleViewSet, ParticipantViewSet

router = DefaultRouter()
router.register('movie', MovieViewSet, basename='prodcuts')
router.register('tags', TagViewSet, basename='tags')
router.register('participant', ParticipantViewSet, basename='participant')
router.register('title', TitleViewSet, basename='title')



urlpatterns = router.urls