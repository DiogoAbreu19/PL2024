from Produto import *
from tabulate import tabulate
from datetime import datetime
import ply.lex as lex

class MaquinaVendas(object):

    tokens = (
        'VALOR',
        'LISTAR',
        'SAIR',
        'COD',
        'SALDO',
    )

    states = (
        ('inserirmoeda', 'exclusive'),
        ('selecionarproduto', 'exclusive')
    )

    t_inserirmoeda_ignore = ', \t\n'

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ANY_ignore = ' \t\n'

    def t_SALDO(self, t):
        r'(?i:saldo)'
        self.imprimeSaldo()

        return t

    def t_LISTAR(self, t):
        r'(?i:listar)'
        self.listaProdutos()

    def t_begin_inserirmoeda(self, t):
        r'(?i:moeda)'
        t.lexer.begin('inserirmoeda')

    def t_inserirmoeda_VALOR(self, t):
        r'2e|1e|50c|20c|10c|5c|2c|1c'
        if t.value[-1] == 'e':
            t.value = int(t.value[:-1])
        elif t.value[-1] == 'c':
            t.value = int(t.value[:-1]) / 100

        self.saldo += t.value 

        return t

    def t_inserirmoeda_exit(self, t):
        r'\.'
        self.imprimeSaldo()
        t.lexer.begin('INITIAL')

    def t_begin_selecionarproduto(self, t):
        r'(?i:selecionar)'
        t.lexer.begin('selecionarproduto')

    def t_selecionarproduto_COD(self, t):
        r'[A-Z][0-9]{2}'
        t.lexer.begin('INITIAL')
        for produto in self.stock:
            if produto.cod == t.value:
                if produto.quant <= 0:
                    print(f"Produto {produto.nome} esgotado")
                    return t
                if produto.preco > self.saldo:
                    print(f"Saldo insuficiente para \"{produto.nome}\" (necessita de {produto.preco}€)")
                    self.imprimeSaldo()
                    return t

                self.saldo -= produto.preco
                produto.quant -= 1
                print(f"Pode retirar o produto dispensado \"{produto.nome}\"")
                self.imprimeSaldo()
                return t
        
        print("Produto inexistente")
        return t

    def t_ANY_error(self, t):
        print("Caractere ilegal '%s'" % t.value[0])
        t.lexer.skip(1)

    def t_SAIR(self, t):
        r'(?i:sair)'
        self.sair = True

        self.despedida()

        return t

    def __init__(self):
        self.lexer = None
        self.sair = False
        self.stock = []
        self.saldo = 0

    def guardaStock(self):
        stock = carregaStock()
        self.stock = stock

    def getStock(self):
        return self.stock

    def imprimeSaldo(self):
        print(f'Saldo = {self.saldo:.2f}€')

    def atualizaSaldo(self, valor):
        self.saldo += valor

    def apresentacao(self):
        d = datetime.now()
        print(f'{d.strftime("%Y-%m-%d")}, Stock carregado, Estado atualizado.')
        print("Bom dia. Estou disponível para atender o seu pedido.")

    def listaProdutos(self):
       print(tabulate([(produto.cod, produto.nome, produto.quant, produto.preco) for produto in self.stock], headers=["Cod", "Nome", "Quantidade", "Preço €"]))

    def despedida(self):
        print(f"Retire o seu troco de {self.saldo:.2f}€.")
        print("Volte sempre!")

    def build(self, **kwargs):
        self.lexer = lex.lex(object=self, **kwargs)
        self.apresentacao()
        self.guardaStock()

    def input(self, data):
        self.lexer.input(data)

    def token(self):
        return self.lexer.token()