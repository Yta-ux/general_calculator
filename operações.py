c=( '\033[m',#0 Cor branca
    '\033[0;31m',#1 Cor vermelha
    '\033[0;32m',#2 Cor verde
    '\033[0;33m',#3 Cor Amarelo
    '\033[0;34m',#4 Cor Azul
    '\033[0;35m',#5 Cor Lilas
    '\033[0;36m',#6 Cor Azul Claro
    '\033[0;37m',#7 Cor Cinza
    )

from math import *
from time import *


def lin(l=42):
    print(f'{c[2]}~{c[0]}'*l)


def cabeçalho(msg):
    lin()
    print(f'{msg:^42}',flush=True)
    lin()


def menu(lis):
    cabeçalho(f'{c[6]}      MENU PRINCIPAL{c[0]}')
    i=1
    for x in lis:
        sleep(1)
        print(f'{c[2]}{i}-{c[6]}{x}{c[0]}')
        i+=1
    sleep(0.5)
    lin()
    sleep(0.8)


def men(lis):
    i=1
    for x in lis:
        sleep(0.8)
        print(f'{c[2]}{i}-{c[6]}{x}{c[0]}')
        i+=1
    sleep(8)
    lin()


def soma():
    sleep(1)
    cabeçalho(f'{c[6]}      ADIÇÃO{c[0]}')
    try:
        sleep(1)
        q = int(input('Quantidade de Números:'))
        s = 0
        for x in range(0, q):
            sleep(0.5)
            so = input(f'{x+1}º Valor:').replace(',','.')
            v = float(so)
            s += v
        sleep(0.5)
        print('Processando...')
        sleep(3)
        print(f'Soma ou Resultado: {s}')
        sleep(1)
    except :
        print(f'{c[1]}Dados Inválidos !{c[0]}')
        sleep(1)


def sub():
    cabeçalho(f'{c[6]}      SUBTRAÇÃO{c[0]}')
    try:
        sleep(1)
        q = int(input('Quantidade de Números:'))
        num=[]
        for y in range(0,q):
            sleep(0.5)
            su=input(f'{y+1}º Valor:').replace(',','.')
            v = float(su)
            num.append(v)
        s=num[0]
        num.pop(0)
        for x in num:
            s-=x
        sleep(0.5)
        print('Processando...')
        sleep(3)
        print(f'Diferença: {s}')
    except:
        print(f'{c[1]}Dados Inválidos !{c[0]}')
    sleep(1)


def multi():
    cabeçalho(f'{c[6]}      MUTIPLICAÇÃO{c[0]}')
    try:
        sleep(1)
        q = int(input('Quantidade de Números:'))
        s = 1
        for x in range(0, q):
            sleep(0.5)
            so = input(f'{x+1}º Valor:').replace(',','.')
            v = float(so)
            s *= v
        sleep(0.5)
        print('Processando...')
        sleep(3)
        print(f'Produto: {s}')
        sleep(1)
    except:
        print(f'{c[1]}Dados Inválidos !{c[0]}')
        sleep(1)


def div():
    cabeçalho(f'{c[6]}      DIVISÃO{c[0]}')
    try:
        sleep(1)
        d = input('Dividendo:').replace(',','.')
        sleep(1)
        di = input('Divisor:').replace(',','.')
        v = float(d)
        v1 = float(di)
        div= v / v1
        r= v % v1
        sleep(0.5)
        print('Processando...')
        sleep(3)
        print( f'''Quociente: {div}
Resto: {r}''')
    except:
        print('Dados Inválidos !')
    sleep(1)


def exp():
    cabeçalho(f'{c[6]}      POTÊNCIA{c[0]}')
    try:
        sleep(1)
        b = input('Base:').replace(',','.')
        sleep(1)
        e = input('Expoente:').replace(',','.')
        v = float(b)
        v1 = float(e)
        p = v ** v1
        sleep(0.5)
        print('Processando...')
        sleep(3)
        print(f'Resulado: {p}')
    except:
        print('Dados Inválidos !')
    sleep(1)


def rad():
    cabeçalho(f'{c[6]}      RAIZ QUADRADA{c[0]}')
    try:
        sleep(1)
        r=input('Radical:').replace(',','.')
        v = float(r)
        ra = sqrt(v)
        sleep(0.5)
        print('Processando...')
        sleep(3)
        print(f'Raiz: {ra:.1f}')
    except:
        print('Dados Inválidos !')
    sleep(1)


def sen():
    cabeçalho(f'{c[6]}      SENO{c[0]}')
    try:
        sleep(1)
        s=input('Ângulo:').replace(',','.')
        v = float(s)
        se=sin(radians(v))
        sleep(0.5)
        print('Processando...')
        sleep(3)
        print(f'Seno: {se:.2f}°')
    except:
        print('Dados Inválidos !')
    sleep(1)


def  cose():
    cabeçalho(f'{c[6]}      COSSENO{c[0]}')
    try:
        sleep(1)
        co=input('Ângulo:').replace(',','.')
        v = float(co)
        s=cos(radians(v))
        sleep(0.5)
        print('Processando...')
        sleep(3)
        print(f'Cossseno: {s:.2f}°')
    except:
        print('Dados Inválidos !')
    sleep(1)


def tang():
    cabeçalho(f'{c[6]}      TANGENTE{c[0]}')
    try:
        sleep(1)
        ta=input('Ângulo:').replace(',','.')
        v = float(ta)
        t=tan(radians(v))
        sleep(0.5)
        print('Processando...')
        sleep(3)
        print(f'Tangente: {t:.2f}°')
    except:
        print('Dados Inválidos !')
    sleep(1)


def pit():
    cabeçalho(f'{c[6]}      TEOREMA DE PITÁGORAS{c[0]}')
    try:
        sleep(1)
        v = input('Hipotenuza:').replace(',','.')
        sleep(0.5)
        v1 = input('Cateto 1 :').replace(',','.')
        sleep(0.5)
        v2 = input('Cateto 2 :').replace(',','.')
        h = float(v)
        c1 = float(v1)
        c2 = float(v2)
        if h == 0:
            hi = ((c1 ** 2) + (c2 ** 2)) ** (1 / 2)
            sleep(0.5)
            print('Processando...')
            sleep(3)
            print(f'Hipotenuza: {hi:.1f}')
        elif c1 == 0:
            ca = ((h ** 2) - (c2 ** 2)) ** (1 / 2)
            sleep(0.5)
            print('Processando...')
            sleep(3)
            print(f'Cateto 1: {ca:.1f}')
        elif c2 == 0:
            ca = ((h ** 2) - (c1 ** 2)) ** (1 / 2)
            sleep(0.5)
            print('Processando...')
            sleep(3)
            print(f'Cateto 2: {ca:.1f}')
    except:
        print('Dados Inválidos')
    sleep(1)


def area():
    cabeçalho(f'{c[6]}      ÁREA DE FIGURAS PLANAS{c[0]}')
    men(['Quadrado','Triâgulo','Retângulo','Circuferência'])
    try:
        f=int(input('Figura:'))
        sleep(1)
        if f == 1:
            v = input('Lado:').replace(',', '.')
            l = float(v)
            q = l ** 2
            sleep(0.5)
            print('Processando...')
            sleep(3)
            print(f'Área do Quadrado: {q}m²')
        elif f == 2:
            sleep(0.5)
            v = input('Base:').replace(',', '.')
            sleep(0.5)
            v1 = input('Altura:').replace(',', '.')
            b = float(v)
            h = float(v1)
            t = (b * h) / 2
            sleep(0.5)
            print('Processando...')
            sleep(3)
            print(f'Área do Triângulo: {t}m²')
        elif f == 3:
            sleep(0.5)
            v = input('Base:').replace(',', '.')
            sleep(0.5)
            v1 = input('Altura:').replace(',', '.')
            b = float(v)
            h = float(v1)
            r = b * h
            sleep(0.5)
            print('Processando...')
            sleep(3)
            print(f'Área do Retângulo: {r}m²')
        elif f == 4:
            sleep(0.5)
            v = input('Raio:').replace(',', '.')
            sleep(0.5)
            v1 = input('Valor de PI:').replace(',', '.')
            r = float(v)
            p = float(v1)
            j = p * (r ** 2)
            sleep(0.5)
            print('Processando...')
            sleep(3)
            print(f'Área da Circuferência: {j}m²')
    except:
        print('Dados Inválidos!')
    sleep(1)

def ext():
    cabeçalho(f'{c[1]}      SAINDO...ATÉ LOGO')
    sleep(2)
