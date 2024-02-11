## TPC1 

Neste TPC decidi utilizar uma classe *Person* para representar as pessoas no CSV dado. 
No ficheiro *main.py*, começa-se por estabelecer uma lista vazia (people) onde se guardará as informações relativas de cada pessoa, um set *modalities* que guardará as modalidades excluindo já aquelas que já se encontram guardadas nesta estrutura de dados e um dicionário *tiers* que guardará as informações das pessoas pertencentes a cada escalão estabelecido.

Temos então duas funções principais:
- **parseCSV** que lê o ficheiro csv, regista as modalidades no *set* e guarda as informações das pessoas em *people* 
- **parseInfo**: que lê o array *people* e faz os cálculos dos atletas aptos e inaptos, bem como popula o dicionário com as pessoas de acordo com o seu escalão

Por fim, temos a main que imprime no terminal as informações desejadas.