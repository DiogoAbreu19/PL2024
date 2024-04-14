import json
from MaquinaVendas import *

class Produto:

    def __init__(self, cod, nome, quant, preco):
        self.cod = cod
        self.nome = nome
        self.quant = quant
        self.preco = preco 

    def __str__(self) -> str:
        return f'Cod: {self.cod} | Nome: {self.nome} | Quant: {self.quant} | Preço: {self.preco}'

def carregaStock() -> [Produto]:

    with open("stock.json", encoding='utf-8') as f:
        d = json.load(f)

    f.close()
    stock = []

    for produto in d:
        novoproduto = Produto(produto['cod'], produto['nome'], produto['quant'], produto['preço'])
        stock.append(novoproduto)

    return stock

    

    
    
