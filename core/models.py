from django.db import models

# Create your models here.
class Article(models.Model):
    serie_enum = (
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('Ti', 'Ti'),
        ('Chinois', 'Chinois'),
        ('All', 'All'),
        ('Esp', 'Esp'),
        ('Italien' , 'Italien'),
        ('Aucun', 'Aucun'),
    )
    classe_enum = (
        ('1ère Maternelle', '1ère Maternelle'),
        ('2éme Maternelle', '2éme Maternelle'),
        ('SIL', 'SIL'),
        ('CP', 'CP'),
        ('CE1', 'CE1'),
        ('CE2', 'CE2'),
        ('CM1', 'CM1'),
        ('CM2', 'CM2'),
        ('Class 1', 'Class 1'),
        ('Class 2', 'Class 2'),
        ('Class 3', 'Class 3'),
        ('Class 4', 'Class 4'),
        ('Class 5', 'Class 5'),
        ('Class 6', 'Class 6'),
        ('6', '6'),
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
        ('Tle', 'Tle'),
        ('From 1', 'From 1'),
        ('From 2', 'From 2'),
        ('From 3', 'From 3'),
        ('From 4', 'From 4'),
        ('From 5', 'From 5'),
        ('From 6', 'From 6'),
        ('From 7', 'From 7'),
        ('Aucun', 'Aucun')

    )
    titre = models.CharField(max_length=2000)
    prix = models.CharField(max_length=200)
    classe = models.CharField(max_length=2000 , choices = classe_enum , blank=True)
    serie = models.CharField(max_length=2000 , choices = serie_enum , blank=True)
    image = models.ImageField(upload_to='manuels',blank=True)
    francophone = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

class LivrePrimaire(Article):
    matiere_enum = (
        ('Mathematiques' , 'Mathematiques'),
        ('Langage' , 'Langage'),
        ('Dessin-peinture-coloriage' , 'Dessin-peinture-coloriage'),
        ('TIC' , 'TIC'),
        ('Sciences et Technologies' , 'Sciences et Technologies'),
        ('Sciences à la citoyenneté' , 'Sciences à la citoyenneté'),
        ('Français' , 'Français'),
        ('Ecriture' , 'Ecriture'),
        ('Anglais' , 'Anglais'),
        ('Sciences Humaines et Sociales' , 'Sciences Humaines et Sociales'),
        ('Litterature' , 'Litterature'),
    )
    matiere = models.CharField(max_length=2000 , choices=matiere_enum)
    editeur = models.CharField(max_length=2000 , blank=True)
    class Meta :
        verbose_name = "LivrePrimaire"
        verbose_name_plural = "LivrePrimaires"

class LivreSecondaire(Article):
    matiere_enum = (
        ('Langue Française', 'Langue Française'),
        ('Litterature', 'Litterature'),
        ('Anglais', 'Anglais'),
        ('Histoire', 'Histoire'),
        ('Geographie', 'Geographie'),
        ('Education à la citoyenneté', 'Education à la citoyenneté'),
        ('Langue et culture nationale', 'Langue et culture nationale'),
        ('Art', 'Art'),
        ('Mathematiques', 'Mathematiques'),
        ('Sciences', 'Sciences'),
        ('Informatique', 'Informatique'),
        ('Latin', 'Latin'),
        ('Langues Etrangère', 'Langues Etrangère'),
        ('SVT', 'SVT'),
        ('PCT', 'PCT'),
        ('Philosophie', 'Philosophie'),
        ('Physique', 'Physique'),
        ('Chimie', 'Chimie'),
        ('Arts cinematographiques', 'Arts cinematographiques'),
        ('Sciences Tles Litteraires', 'Sciences Tles Litteraires'),
    )
    matiere = models.CharField(max_length=2000 , choices=matiere_enum)
    auteur = models.CharField(max_length=2000 , blank=True)
    editeur = models.CharField(max_length=2000 , blank=True)
    class Meta :
        verbose_name = "LivreSecondaire"
        verbose_name_plural = "LivreSecondaires"

class Cahiers(Article):
    nbre_page = models.CharField(max_length=2000)
    contenu_paquets = models.CharField(max_length=2000 , blank=True)
    cartonne =  models.BooleanField(default=False)
    class Meta :
        verbose_name = "Cahiers"
        verbose_name_plural = "Cahiers"

class Accessoire(Article):
    contenu_paquets = models.CharField(max_length=2000 , blank=True)
    class Meta :
        verbose_name = "Accessoire"
        verbose_name_plural = "Accessoires"

class User(models.Model):
    nom = models.CharField(max_length=255)
    prenom =models.CharField(max_length=255 , blank=True)
    residence = models.CharField(max_length=255)
    contact  = models.CharField(max_length=30 , unique=True)
    email = models.CharField(max_length=255, unique=True )
    password = models.CharField(max_length=255)
    developpeur =  models.BooleanField(default=False)
    testeur =  models.BooleanField(default=False)
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Panier(models.Model):
    article_id = models.ForeignKey(Article , on_delete=models.CASCADE)
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    prix = models.CharField(max_length=255)
    envoye_commande = models.BooleanField(default=False)
    class Meta:
        verbose_name = "Panier"
        verbose_name_plural = "Paniers"


class Commande(models.Model):
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    liste = models.CharField(max_length=2000000 , blank=True)
    date_commande = models.DateTimeField()
    montant = models.CharField(max_length=255)
    livré = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"
