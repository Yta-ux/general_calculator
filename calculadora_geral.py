from operações import *
from time import sleep

while True:
    menu(['Adição', 'Subtração', 'Multiplicação', 'Divisão', 'Potenciação', 'Raiz Quadrada','Seno','Cosseno','Tangente','Teorema de Pitágoras','Área de Figuras Planas','Sair'])
    al = int(input('Alternativa:'))
    sleep(1)
    if al == 1:
        soma()

    elif al == 2:
        sub()

    elif al == 3 :
        multi()

    elif al == 4:
        div()

    elif al == 5:
        exp()

    elif al == 6:
        rad()

    elif al == 7:
        sen()

    elif al == 8:
        cose()

    elif al == 9:
        tang()

    elif al == 10:
        pit()

    elif al == 11:
        area()

    elif al == 12:
        ext()
        break