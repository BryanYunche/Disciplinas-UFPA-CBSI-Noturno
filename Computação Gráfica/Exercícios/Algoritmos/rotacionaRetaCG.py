from desenhaRetaCG import *
from mudaPosicao import *
import math

def senoCossenoAngulo(graus):
    # Converter o ângulo para radianos
    angulo_radianos = math.radians(graus)

    # Calcular o seno e o cosseno
    seno = math.sin(angulo_radianos)
    cosseno = math.cos(angulo_radianos)

    return seno, cosseno

def calculaRotacaoPonto(x, y, seno, cosseno):
    xR = x * cosseno - y * seno
    yR = x * seno + y * cosseno

    return xR, yR


def desenhaRetaRotacionada(x1, y1, x2, y2, graus):
    #Calcula Seno e Cosseno
    seno, cosseno = senoCossenoAngulo(graus)

    # Calcula a rotação para Ponto 01 e Ponto 02
    x1R, y1R = calculaRotacaoPonto(x1, y1, seno, cosseno)
    x2R, y2R = calculaRotacaoPonto(x2, y2, seno, cosseno)

    # Arredonda os valores de x1R, y1R, x2R e y2R para o inteiro mais próximo
    x1R = round(x1R)
    y1R = round(y1R)
    x2R = round(x2R)
    y2R = round(y2R)

    pontosRotacionados = desenhaReta(x1R, y1R, x2R, y2R)

    return pontosRotacionados

def coeficienteAngularRotacionada(x1, y1, x2, y2, graus):
    # Calcula Seno e Cosseno
    seno, cosseno = senoCossenoAngulo(graus)

    # Calcula a rotação para Ponto 01 e Ponto 02
    x1R, y1R = calculaRotacaoPonto(x1, y1, seno, cosseno)
    x2R, y2R = calculaRotacaoPonto(x2, y2, seno, cosseno)

    # Arredonda os valores de x1R, y1R, x2R e y2R para o inteiro mais próximo
    x1R = round(x1R)
    y1R = round(y1R)
    x2R = round(x2R)
    y2R = round(y2R)

    dx = x2R - x1R
    dy = y2R - y1R
    m = round(dy / dx, 1)

    return m

def desenhaRetaRotacionadaPivo(x1P, y1P, x2, y2, graus):
    #Calcula Seno e Cosseno
    seno, cosseno = senoCossenoAngulo(graus)

    #Calcula pivo
    tx, ty = calculaPivo(x1P, y1P)

    #Tras a reta para 0 antes de rotacionar
    x1R, y1R = mudaPonto(x1P, y1P, tx, ty)
    x2R, y2R = mudaPonto(x2, y2, tx, ty)

    # Calcula a rotação para Ponto 01 e Ponto 02
    x1R, y1R = calculaRotacaoPonto(x1P, y1P, seno, cosseno)
    x2R, y2R = calculaRotacaoPonto(x2, y2, seno, cosseno)

    # Arredonda os valores de x1R, y1R, x2R e y2R para o inteiro mais próximo
    x1R = round(x1R)
    y1R = round(y1R)
    x2R = round(x2R)
    y2R = round(y2R)

    pontosRotacionados = desenhaReta(x1R, y1R, x2R, y2R)

    return pontosRotacionados


