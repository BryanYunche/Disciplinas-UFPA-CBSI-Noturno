import desenhaRetaCG as rt

def desenhaTriangulo(xa, ya, xb, yb, xc, yc):
    aresta01 = rt.desenhaReta(xa, ya, xb, yb)
    aresta02 = rt.desenhaReta(xb, yb, xc, yc)
    aresta03 = rt.desenhaReta(xc, yc, xa, ya)


    triangulo = aresta01 + aresta02 + aresta03

    return triangulo