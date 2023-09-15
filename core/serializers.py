from rest_framework.serializers import ModelSerializer , Serializer
from core.models import *

class ArticleSerializer(ModelSerializer):

    class Meta :
        model = Article
        fields = [ 'id','titre' ,'prix' ,'classe','serie', 'image' , 'francophone']

class LivrePrimaireSerializer(ModelSerializer):

    class Meta :
        model = LivrePrimaire
        fields = [ 'id' ,'titre' ,'prix' ,'classe','serie', 'image' , 'francophone' , 'matiere' ,'editeur']

class LivreSecondaireSerializer(ModelSerializer):

    class Meta :
        model = LivreSecondaire
        fields = [ 'id' ,'titre' ,'prix' ,'classe','serie', 'image' , 'francophone' ,'matiere' ,'auteur' ,'editeur']

class CahiersSerializer(ModelSerializer):

    class Meta :
        model = Cahiers
        fields = [ 'id' ,'titre' ,'prix' ,'classe','serie', 'image' , 'francophone'  ,'nbre_page' ,'contenu_paquets' ,'cartonne']

class AccessoireSerializer(ModelSerializer):

    class Meta :
        model = Accessoire
        fields = [ 'id' ,'titre' ,'prix' ,'classe','serie', 'image' , 'francophone' ,'contenu_paquets']



class UserSerializer(ModelSerializer):

    class Meta :
        model = User
        fields = [ 'id','nom' , 'prenom' , 'residence','contact', 'email' , 'password' , 'developpeur' , 'testeur']

class PanierSerializer(ModelSerializer):
    class Meta :
        model = Panier
        fields = [ 'id','article_id','user_id', 'quantite' , 'prix' , 'envoye_commande']

class CommandeSerializer(ModelSerializer):
    class Meta :
        model = Commande
        fields = [ 'id','user_id' ,'liste' , 'date_commande' , 'montant', 'livré']