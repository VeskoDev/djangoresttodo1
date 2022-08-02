from rest_framework.routers import DefaultRouter  

from .views import MovieViewSet, TagViewSet, TitleViewSet, ParticipantViewSet 
#LanguageView, ParadigmView, ProgrammerView

router = DefaultRouter()
router.register('movie', MovieViewSet)
router.register('tags', TagViewSet)
router.register('participant', ParticipantViewSet)
router.register('title', TitleViewSet)

# router.register('languages', LanguageView)
# router.register('paradigm', ParadigmView)
# router.register('programmer', ProgrammerView)




urlpatterns = router.urls