from rest_framework.routers import DefaultRouter
from core.api_views import *

router = DefaultRouter()

router.register(r'article', ArticleViewset, basename='article')
router.register(r'serie', SerieViewset, basename='serie')
router.register(r'niveau', NiveauViewset, basename='niveau')
router.register(r'user', UserViewset, basename='user')
router.register(r'commande', CommandeViewset, basename='commande')


urlpatterns = [ 
]
urlpatterns += router.urls