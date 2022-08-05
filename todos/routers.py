from rest_framework.routers import DefaultRouter  

from .views import MovieViewSet, SlikeView, TitleViewSet, ParticipantViewSet, PrikazSlikaView, TagView #TagViewSet
#LanguageView, ParadigmView, ProgrammerView

router = DefaultRouter()
router.register('movie', MovieViewSet)
#router.register('tags', TagViewSet)
router.register('participant', ParticipantViewSet)
router.register('title', TitleViewSet)
router.register('slike', SlikeView)
router.register('prikazslike', PrikazSlikaView)
router.register('tags', TagView)


# router.register('languages', LanguageView)
# router.register('paradigm', ParadigmView)
# router.register('programmer', ProgrammerView)




urlpatterns = router.urls