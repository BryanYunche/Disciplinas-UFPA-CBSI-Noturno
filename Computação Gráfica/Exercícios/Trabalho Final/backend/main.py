import desenhaRetaCG as rt
import desenhaMatriz as ap
import quadrilatero as qd
import triangulo as tr
import poligonoQualquer as pl

# #Desenha uma reta na horizontal
# reta = rt.bresenham_line(3, 5, 7, 5)
# print(reta)
# ap.desenhar_linha_entre_pontos(reta)
#
# #Desenha uma reta na horizontal invertida
# reta = rt.bresenham_line(7, 5, 3, 5)
# print(reta)
# ap.desenhar_linha_entre_pontos(reta)
#
# #Desenha uma reta na vertical
# reta = rt.bresenham_line(3, 5, 3, 9)
# print(reta)
# ap.desenhar_linha_entre_pontos(reta)
#
# #Desenha uma reta na vertical invertida
# reta = rt.bresenham_line(3, 9, 3, 5)
# print(reta)
# ap.desenhar_linha_entre_pontos(reta)
#
# # Reta com inclinação positiva em quadrante I
# reta = rt.bresenham_line(1, 1, 5, 4)
# print(reta)
# ap.desenhar_linha_entre_pontos(reta)
#
# # Reta com inclinação negativa em quadrante II
# reta = rt.bresenham_line(-1, 1, -5, 4)
# print(reta)
# ap.desenhar_linha_entre_pontos(reta)
#
# # Reta com inclinação positiva em quadrante III
# reta = rt.bresenham_line(-1, -1, -5, -4)
# print(reta)
# ap.desenhar_linha_entre_pontos(reta)
#
# # Reta com inclinação negativa em quadrante IV
# reta = rt.bresenham_line(1, -1, 5, -4)
# print(reta)
# ap.desenhar_linha_entre_pontos(reta)
#
# # Reta vertical invertida em quadrante II
# reta = rt.bresenham_line(-5, 1, -5, 5)
# print(reta)
# ap.desenhar_linha_entre_pontos(reta)
#
# # Reta horizontal invertida em quadrante III
# reta = rt.bresenham_line(-5, -5, -1, -5)
# print(reta)
# ap.desenhar_linha_entre_pontos(reta)
#
# #-----------------------------------------------
# #Exemplo de quadrado
# quadrado = qd.desenhaQuadrilatero(1, 2, 1, 6, 6, 6, 6, 2)
# print(quadrado)
# ap.desenhar_linha_entre_pontos(quadrado)
#
# #Exemplo de triangulo
# triangulo = tr.desenhaTriangulo(-10, 6, 10, 0, -3, -7)
# ap.desenhar_linha_entre_pontos(triangulo)
#
# #Exemplo de triangulo
# triangulo = tr.desenhaTriangulo(4, 7, 7, 2, 1, 2)
# ap.desenhar_linha_entre_pontos(triangulo)
#
# #-----------------------------------------------
# poligono = pl.poligonoQualquer(4, 1, 2, 1, 6, 6, 6, 6, 2)
# print(poligono)
# ap.desenhar_linha_entre_pontos(poligono)
#
# poligono = pl.poligonoQualquer(3, -10, 6, 10, 0, -3, -7)
# print(poligono)
# ap.desenhar_linha_entre_pontos(poligono)
#
# poligono = pl.poligonoQualquer(3, 4, 7, 7, 2, 1, 2)
# print(poligono)
# ap.desenhar_linha_entre_pontos(poligono)

poligono = pl.poligonoQualquer(5, 0,-7, 5,-3, 3,4, -3,4, -5,-3)
print(poligono)
ap.desenhar_linha_entre_pontos(poligono)

# poligono = pl.poligonoQualquer(5, 0,-3, 2,-1, 3,2, 0,4, -3,2)
# print(poligono)
# ap.desenhar_linha_entre_pontos(poligono)













