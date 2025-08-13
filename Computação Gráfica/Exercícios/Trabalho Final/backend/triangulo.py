import desenhaRetaCG as rt

def desenhaTriangulo(xa, ya, xb, yb, xc, yc):
    aresta01 = rt.bresenham_line(xa, ya, xb, yb)
    aresta02 = rt.bresenham_line(xb, yb, xc, yc)
    aresta03 = rt.bresenham_line(xc, yc, xa, ya)


    triangulo = aresta01 + aresta02 + aresta03

    return triangulo