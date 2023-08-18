from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (CreateModelMixin , UpdateModelMixin , ListModelMixin , RetrieveModelMixin , DestroyModelMixin)
from core.serializers import *
from core.models import  *



class ArticleViewset(CreateModelMixin ,UpdateModelMixin ,ListModelMixin , RetrieveModelMixin ,DestroyModelMixin , GenericViewSet):

    serializer_class = ArticleSerializer


    def get_queryset(self):
        return Article.objects.all()
    

class SerieViewset(CreateModelMixin ,UpdateModelMixin ,ListModelMixin , RetrieveModelMixin ,DestroyModelMixin , GenericViewSet):

    serializer_class = SerieSerializer


    def get_queryset(self):
        return Serie.objects.all()
    

class NiveauViewset(CreateModelMixin ,UpdateModelMixin ,ListModelMixin , RetrieveModelMixin ,DestroyModelMixin , GenericViewSet):

    serializer_class = NiveauSerializer


    def get_queryset(self):
        return Niveau.objects.all()
    

class UserViewset(CreateModelMixin ,UpdateModelMixin ,ListModelMixin , RetrieveModelMixin ,DestroyModelMixin , GenericViewSet):

    serializer_class = UserSerializer


    def get_queryset(self):
        return User.objects.all()
    

class CommandeViewset(CreateModelMixin ,UpdateModelMixin ,ListModelMixin , RetrieveModelMixin ,DestroyModelMixin , GenericViewSet):

    serializer_class = CommandeSerializer


    def get_queryset(self):
        return Commande.objects.all()
    
