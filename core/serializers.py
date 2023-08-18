from rest_framework.serializers import ModelSerializer , Serializer
from core.models import *

class ArticleSerializer(ModelSerializer):

    class Meta :
        model = Article
        fields = [ 'id','matiere' ,'nom' ,'editeur','prix' , 'image']



class SerieSerializer(ModelSerializer):

    class Meta :
        model = Serie
        fields = [ 'id','article' ,'choice']

class NiveauSerializer(ModelSerializer):

    class Meta :
        model = Niveau
        fields = [ 'id','article' ,'choice']

class UserSerializer(ModelSerializer):

    class Meta :
        model = User
        fields = [ 'id','nom' ,'prenom','email', 'contact_1' , 'contact_2' , 'residence' , 'password']

class CommandeSerializer(ModelSerializer):

    class Meta :
        model = Commande
        fields = [ 'id','article' ,'user','date', 'longitude' , 'latitute' , 'prix']