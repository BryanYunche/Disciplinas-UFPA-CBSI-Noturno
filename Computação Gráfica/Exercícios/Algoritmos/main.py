import desenhaRetaCG as rt
import desenhaMatriz as ap
import quadrilatero as qd
import triangulo as tr
import poligonoQualquer as pq

#Desenha uma reta na horizontal
#reta = rt.desenhaReta(3, 5, 7, 5)

#Desenha uma reta na vertical
#reta = rt.desenhaReta(3, 5, 3, 9)
#ap.desenhar_linha_entre_pontos(reta)

#desenha um quadrilatero
quadrado = qd.desenhaQuadrilatero(3, 2, 3, 6, 7, 6, 7, 2)
#print(quadrado)
ap.desenhar_linha_entre_pontos(quadrado)

#Desenha um quadrado com uma função de desenho qualquer
poligono = pq.poligonoQualquer(5, 3, 4, 5, 8, 8, 7, 9, 4, 6, 1)
ap.desenhar_linha_entre_pontos(poligono)

#Desenha triangulo
#tri = tr.desenhaTriangulo(1, 2, 4, 7, 7, 2)
#ap.desenhar_linha_entre_pontos(tri)

#Desenha um quadrado com uma função de desenho qualquer
poligono2 = pq.poligonoQualquer(3, 1, 2, 4, 7, 7, 2)
ap.desenhar_linha_entre_pontos(poligono2)

#Desenha reta decrescente
#reta = rt.desenhaReta(4, 7, 7, 2)
#print(rt.calculaCoeficienteAngular(4, 7, 7, 2))
#ap.desenhar_linha_entre_pontos(reta)

#desenha reta debaixo
#reta01 = rt.desenhaReta(7, 2, 3, 2)
#print(reta01)
#ap.desenhar_linha_entre_pontos(reta01)

#print(rt.calculaCoeficienteAngular(7, 2, 3, 2))
#Trás a reta para o zero
#retaNoZero = rt.desenhaRetaPivo(3, 5, 7, 9)
#ap.desenhar_linha_entre_pontos(retaNoZero)

#Desenha reta normal
reta = rt.desenhaReta(1, 2, 4, 7)
ap.desenhar_linha_entre_pontos(reta)













