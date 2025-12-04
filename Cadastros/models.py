from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=50)
                                     
    idade = models.PositiveIntegerField()

    raça = models.CharField(max_length = 40)

    especieAnimal = models.CharField(max_length = 50)

    class Meta:
        verbose_name = "Animal"          
        verbose_name_plural = "Animais"  
        ordering = ['-id']                                    

    def __str__(self):
        return self.nome                                                      


class Dono(models.Model):
    nome = models.CharField(max_length=50)                              
    email = models.EmailField()                                                             
    telefone = models.CharField(max_length = 11)
    endereco = models.CharField(max_length = 100)             

    def __str__(self):                                                      
        return self.nome                                                  
    
    
class Adocao(models.Model):
    Animal = models.ForeignKey(Animal, on_delete=models.CASCADE)              
    Dono = models.ForeignKey(Dono, on_delete=models.CASCADE)              
    data_Adocao = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Adoção"          
        verbose_name_plural = "Adoções"  
        ordering = ['-id']                     

    def __str__(self):                                                      
        return f"{self.Animal.nome} adotado por {self.Dono.nome}" 
