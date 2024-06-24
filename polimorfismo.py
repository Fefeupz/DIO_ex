class Passaro: 
    def voar(self):
        print('Voando...')
        
class Pardal (Passaro):
    def voar (self):
        #super().voar()
        print('Pardal voando...')
            
class Avestruz (Passaro):
    def voar(self):
        print('Avestruz não pode voar.')
    
# Exemplo ruim do uso de herança para "ganhar" o método de voar  
class Aviao (Passaro):
    def voar(self):
        print('Avião está decolando...')
        
def plano_voo(obj):
    obj.voar()
    

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())