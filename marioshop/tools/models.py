from django.db import models
from oscar.core.loading import get_model

Transfer = get_model('oscar_accounts', 'Transfer')


class ToolType(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=256, default='-')
    description = models.CharField(max_length=256)
    value = models.IntegerField()

    def __str__(self):
        return "Ferramenta:{} Tipo:{} Descrição:{} Valor:{}".format(self.name, self.type, self.description, self.value)


class Tool(models.Model):
    name = models.CharField(max_length=256) 
    transfer = models.ForeignKey(Transfer,null=True,blank=True,on_delete=models.SET_NULL)#Nome usuário do colaborador
    type = models.ForeignKey(ToolType, on_delete=models.CASCADE) #ferramenta que o colaborador entregou
    quantity = models.IntegerField()

    @property
    def value(self):    
        peso = 0
        if self.quantity == 1:
            peso = 1
        elif self.quantity == 2:
            peso = 1.2
        elif self.quantity >= 3:
            peso = 1.5
        return self.quantity * self.type.value * peso

    @property
    def username(self):
        return transfer.destination.primary_user.username    

    def __str__(self):
        return "Colaborador:{} Ferramenta:{} Quantidade:{} Valor:{}".format(self.user.username, self.type, self.quantity, self.value)
