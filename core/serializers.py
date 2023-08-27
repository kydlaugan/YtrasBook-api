from rest_framework.serializers import ModelSerializer , Serializer
from core.models import *

class ArticleSerializer(ModelSerializer):

    class Meta :
        model = Article
        fields = [ 'id','matiere' ,'nom' ,'auteur','editeur', 'serie' , 'niveau', 'prix' , 'image']



class UserSerializer(ModelSerializer):

    class Meta :
        model = User
        fields = [ 'id','nom' ,'prenom','email', 'contact_1' , 'contact_2' , 'residence' , 'password']

class PanierSerializer(ModelSerializer):
    class Meta :
        model = Panier
        fields = [ 'id','user','article', 'status' , 'prix' , 'quantite']

class CommandeSerializer(ModelSerializer):
    class Meta :
        model = Commande
        fields = [ 'id','user' ,'date_commande' , 'status', 'prix', 'description','longitude' , 'latitude' ]