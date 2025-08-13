import desenhaRetaCG as rt

def desenhaQuadrilatero(xa, ya, xb, yb, xc, yc, xd, yd):
    aresta01 = rt.desenhaReta(xa, ya, xb, yb)
    aresta02 = rt.desenhaReta(xb, yb, xc, yc)
    aresta03 = rt.desenhaReta(xc, yc, xd, yd)
    aresta04 = rt.desenhaReta(xd, yd, xa, ya)

    quadrilatero = aresta01 + aresta02 + aresta03 + aresta04

    return quadrilatero
