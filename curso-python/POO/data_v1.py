class Data:
    
    def __init__(self, dia=1, mes=9, ano=1970):
        self.dia = dia
        self.mes = mes 
        self.ano = ano
        
    def __str__ (self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2019)
print(d1)

d2 = Data(ano =2022)
print(d2)


