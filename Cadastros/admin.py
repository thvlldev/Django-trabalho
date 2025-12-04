from django.contrib import admin
from .models import Dono, Animal, Adocao

                            


admin.site.site_header = "Administração do Sistema de Cadastros"          
admin.site.site_title = "Administração de Cadastros de adoção"                      
admin.site.register(Animal)                                               
admin.site.register(Dono)                                               
admin.site.register(Adocao)                                           


