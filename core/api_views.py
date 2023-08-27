from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (CreateModelMixin , UpdateModelMixin , ListModelMixin , RetrieveModelMixin , DestroyModelMixin)
from core.serializers import *
from core.models import  *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView




class ArticleViewset(CreateModelMixin ,UpdateModelMixin ,ListModelMixin , RetrieveModelMixin ,DestroyModelMixin , GenericViewSet):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    

class UserViewset(CreateModelMixin ,UpdateModelMixin ,ListModelMixin , RetrieveModelMixin ,DestroyModelMixin , GenericViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

  
  
class PanierViewset(CreateModelMixin ,UpdateModelMixin ,ListModelMixin , RetrieveModelMixin ,DestroyModelMixin , GenericViewSet):

    serializer_class = PanierSerializer
    queryset = Panier.objects.all() 

class CommandeViewset(CreateModelMixin ,UpdateModelMixin ,ListModelMixin , RetrieveModelMixin ,DestroyModelMixin , GenericViewSet):

    serializer_class = CommandeSerializer
    queryset = Commande.objects.all()

    @action(detail=False, methods=['POST'])
    def commander_article(self, request):
        #article = request.data['article']
        #article = request.data['user']
        # Logique personnalisée ici
        data = {'message': 'Fonction personnalisée appelée avec succès'}
        return Response(data)


