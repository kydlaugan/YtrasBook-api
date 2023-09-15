from django.contrib import admin
from core.models import *
# Register your models here.
admin.site.register(Article)
admin.site.register(LivrePrimaire)
admin.site.register(LivreSecondaire)
admin.site.register(Cahiers)
admin.site.register(Accessoire)
admin.site.register(User)
admin.site.register(Panier)
admin.site.register(Commande)

