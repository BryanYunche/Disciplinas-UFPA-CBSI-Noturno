import desenhaRetaCG as rt

def desenhaQuadrilatero(xa, ya, xb, yb, xc, yc, xd, yd):
    aresta01 = rt.bresenham_line(xa, ya, xb, yb)
    aresta02 = rt.bresenham_line(xb, yb, xc, yc)
    aresta03 = rt.bresenham_line(xc, yc, xd, yd)
    aresta04 = rt.bresenham_line(xd, yd, xa, ya)

    quadrilatero = aresta01 + aresta02 + aresta03 + aresta04

    return quadrilatero
