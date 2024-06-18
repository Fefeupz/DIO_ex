class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo 
        self.ano = ano 
        self.valor = valor
        self.marcha = 1
        
    def buzinar (self):
        print("Plim plim!!!")
        
    def parar (self):
        print("Parando a bicicleta...")
        print("Parou.")
        
    def correr(self):
        print("Vraummm...")
        
    def trocar_marcha(self, nro_marcha):
        print("Trocando marcha...")
        
        def _trocar_marcha():
            if nro_marcha > self.marcha:
                print("Marcha trocada.")
            else:
                print("Não foi possível trocar de marcha.")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        
b1 = bicicleta ("Vermelho", "Caloi2000", 2000, 189)
b1.buzinar()
b1.parar()
b1.trocar_marcha(2)
b1.correr()