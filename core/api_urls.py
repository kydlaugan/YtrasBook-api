from rest_framework.routers import DefaultRouter
from django.urls import path
from core.api_views import *

router = DefaultRouter()

router.register(r'article', ArticleViewset, basename='article')
router.register(r'user', UserViewset, basename='user')
router.register(r'panier', PanierViewset, basename='panier')
router.register(r'commande', CommandeViewset, basename='commande')


urlpatterns = [ 
]
urlpatterns += router.urls

    
