import re, sys
from MaquinaVendas import *

def main():
    maquina = MaquinaVendas()
    maquina.build()

    while not maquina.sair:
        data = input(">> ")
        maquina.input(data)

        while True:
            tok = maquina.token()
            if not tok:
                break

if __name__ == "__main__":
    main()

