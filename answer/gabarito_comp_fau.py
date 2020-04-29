## ╔═╗╦═╗╔═╗ ╦ ╦╦╔╦╗╔═╗╔╦╗╦ ╦╦═╗╔═╗
## ╠═╣╠╦╝║═╬╗║ ║║ ║ ║╣  ║ ║ ║╠╦╝╠═╣
## ╩ ╩╩╚═╚═╝╚╚═╝╩ ╩ ╚═╝ ╩ ╚═╝╩╚═╩ ╩
##          LAMO/FAU/UFRJ
##
##        Pedro Maciel Xavier
##      pedromxavier@poli.ufrj.br

## Importando os módulos
import math

## Aula 1 -  Tipos, Variáveis e Funções

## 1.1 As notas muscais
def f(n):
    """ f(n : int) -> int
        Calcula a frequência aproximada (em Hertz) de uma nota a `n` semitons do lá central. 
    """
    return int(round(440.0 * (2 ** (n / 12.0))))

## 1.2 Coordenadas Polares
def polar(x, y):
    """ polar(x : float, y : float) -> (float, float)
        Retorna um par (r, theta) correspondente às coordenadas (x, y) na forma polar.
    """
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x)
    return (r, theta)

def cart(r, theta):
    """ cart(r : float, theta : float) -> (float, float)
        Retorna a coordenada (x, y) correspondente ao par (r, theta) de coordenadas polares.
    """
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)

## 1.3 Números de Fibonacci e a proporção áurea
def F(n):
    """ F(n : int) -> int
        Calcula o `n`-ésimo número de Fibonacci. 
    """
    if n == 0 or n == 1:
        return 1
    else:
        return F(n-2) + F(n-1)

def phi(n):
    """ F(n : int) -> float
        Calcula uma aproximação da razão áurea, com base no `n`-ésimo número de Fibonacci e o seu sucessor.
    """
    return F(n + 1) / F(n)

## Aula 2 - Condicionais

## 2.1 Dentro do círculo
def dentro(x, y):
    """ dentro(x : float, y :float) -> bool
        Retorna True se o ponto (x, y) estiver dentro do círculo de raio 1 com centro em (0, 0).
    """
    return math.sqrt(x ** 2 + y ** 2) <= 1

## 2.2 Intersecção de Retângulos
def intersec(A, B):
    """ intersec(A : tuple[4], B : tuple[4]) -> tuple[4]
        intersec(A : tuple[4], B : tuple[4]) -> None
        Calcula a intersecção de dois retângulos, dados por tuplas de tamanho 4.
    """
    (ax1, ay1, ax2, ay2) = A
    (bx1, by1, bx2, by2) = B

    if ax1 > bx2 or bx1 > ax2:
        return None
    elif ay2 > by1 or by2 > ay1:
        return None
    else:
        cx1 = max(ax1, bx1)
        cy1 = min(ay1, by1)
        cx2 = min(ax2, bx2)
        cy2 = max(ay2, by2)
        C = (cx1, cy1, cx2, cy2)
        return C

## 2.3 Anos Bissextos
def bissexto(ano):
    """ bissexto(ano : int) -> bool
        Se o `àno` for bissexto, retorna True. Retorna False no caso contrário.
    """
    if (ano % 400) == 0:
        return True
    elif (ano % 100) == 0:
        return False
    elif (ano % 4) == 0:
        return True
    else:
        return False

## 2.4 Meia-Entrada
def meia_entrada(idade, estudante, deficiencia, baixa_renda):
    """ meia_entrada(idade : inte, estudante : bool, deficiencia : bool, baixa_renda : bool) -> bool
        Retorna True se a pessoa tiver direito a meia-entrada. Retorna False se a pessoa não tiver direito ao benefício.
    """
    if idade >= 60:
        return True
    elif idade < 21:
        return True
    elif 15 <= idade <= 29:
        if estudante or deficiencia or baixa_renda:
            return True
        else:
            return False
    else:
        return False

## Aula 3 - Listas e Loops

## 3.1 Sequência de Collatz
def f(n):
    """ f(n : int) -> int
        Função geradora da sequência de Collatz.
    """
    if (n % 2) == 0:
        return n // 2
    else:
        return 3 * n + 1

def collatz(n):
    """ collatz(n : int) -> int
        Retorna o comprimento da sequência de Collatz gerada a partir do número `n`. 
    """
    i = 1
    while n > 1:
        n = f(n)
        i = i + 1
    return i

## 3.2 Crivo
def crivo(N):
    """ crivo(N : int) -> list
        Retorna uma lista contendo os números primos entre 0 e `N`.
    """
    L = [True] * (N + 1)
    L[0] = False
    L[1] = False
    i = 2
    while i < (N + 1):
        if L[i]:
            j = 2 * i
            while j < (N + 1):
                L[j] = False
                j = j + i
        i = i + 1
    P = []
    i = 0
    while i < (N + 1):
        if L[i]:
            P.append(i)
        i = i + 1
    return P

## 3.3 Troco
def troco(q):
    """ troco(q : int) -> list
        Retorna quantas moedas de cada usar para dar uma certa quantia `q` de troco. As moedas são de 100 (1 real), 50, 25, 10 e 5 centavos.
    """
    moedas = [100, 50, 25, 10, 5]

    total = q + (5 - (q % 5))

    
    
            
