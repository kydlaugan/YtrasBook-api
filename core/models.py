from django.db import models

# Create your models here.
class Article(models.Model):
    liste = (
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
    specialite = (
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('Ti', 'Ti'),
        ('Chinois', 'Chinois'),
        ('All/Esp', 'All/Esp'),
    )
    classe = (
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
    )
    matiere = models.CharField(max_length=2000 , choices=liste)
    nom = models.CharField(max_length=2000, blank=True)
    auteur = models.CharField(max_length=2000, blank=True)
    editeur = models.CharField(max_length=2000, blank=True)
    serie = models.CharField(max_length=2000 , choices=specialite , blank=True)
    niveau = models.CharField(max_length=2000 , choices= classe , blank=True)
    prix = models.CharField(max_length=200)
    image = models.ImageField(upload_to='manuels',blank=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

# class Serie(models.Model):
#     specialite = (
#         ('C', 'C'),
#         ('D', 'D'),
#         ('E', 'E'),
#         ('Ti', 'Ti'),
#         ('Chinois', 'Chinois'),
#         ('All/Esp', 'All/Esp'),
#     )
#     article = models.ForeignKey(Article , on_delete=models.CASCADE)
#     choice = models.CharField(max_length=255 , choices=specialite)
#     class Meta:
#         verbose_name = "Serie"
#         verbose_name_plural = "Series"



# class Niveau(models.Model):
#     classe = (
#         ('SIL', 'SIL'),
#         ('CP', 'CP'),
#         ('CE1', 'CE1'),
#         ('CE2', 'CE2'),
#         ('CM1', 'CM1'),
#         ('CM2', 'CM2'),
#         ('Class 1', 'Class 1'),
#         ('Class 2', 'Class 2'),
#         ('Class 3', 'Class 3'),
#         ('Class 4', 'Class 4'),
#         ('Class 5', 'Class 5'),
#         ('Class 6', 'Class 6'),
#         ('6', '6'),
#         ('5', '5'),
#         ('4', '4'),
#         ('3', '3'),
#         ('2', '2'),
#         ('1', '1'),
#         ('Tle', 'Tle'),
#     )
#     article = models.OneToOneField(Article , on_delete=models.CASCADE)
#     choice = models.CharField(max_length=255 , choices=classe)
#     class Meta:
#         verbose_name = "Niveau"
#         verbose_name_plural = "Niveaux"


class User(models.Model):
    nom = models.CharField(max_length=255)
    prenom =models.CharField(max_length=255 , blank=True)
    email = models.CharField(max_length=255, unique=True )
    contact_1  = models.CharField(max_length=30 , unique=True)
    contact_2  = models.CharField(max_length=30 , unique=True , blank=True)
    residence = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Panier(models.Model):
    etat = (
        ('En Cours', 'En Cours'),
        ('Livré', 'Livré'),
          )
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    article = models.ForeignKey(Article , on_delete=models.CASCADE)
    status = models.CharField(max_length=255 , choices=etat ,default="En Cours")
    prix = models.CharField(max_length=255)
    quantite = models.IntegerField(default=1)
    class Meta:
        verbose_name = "Panier"
        verbose_name_plural = "Paniers"


class Commande(models.Model):
    etat = (
        ('En Cours', 'En Cours'),
        ('Livré', 'Livré'),
    )
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    date_commande = models.DateTimeField()
   # date_livraison = models.DateField(blank=True)
    status = models.CharField(max_length=255 , choices=etat ,default="En Cours")
    prix = models.CharField(max_length=255)
    description = models.CharField(max_length=200000)
    longitude = models.CharField(max_length=255 , blank=True)
    latitude = models.CharField(max_length=255 , blank=True)
    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"
