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
        
cor = input("Digite a cor da bicicleta: ")
modelo = input("Digite o modelo da bicicleta: ")
ano = int(input("Digite o ano da bicicleta: "))
valor = float(input("Digite o valor da bicicleta: "))

b1 = bicicleta(cor, modelo, ano, valor)
print(b1)
b1.buzinar()
