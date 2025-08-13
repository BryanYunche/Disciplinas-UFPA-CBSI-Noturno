from desenhaRetaCG import desenhaReta

def escalaPonto(x, y, sx, sy):
    xS = x*sx
    yS = y*sy
    return xS, yS

def desenhaRestaEscalada(x1, y1, x2, y2, sx, sy):
    x2E, y2E = x2, y2
    x1E, y1E = x1, y1

    x2E, y2E = escalaPonto(x2E, y2E, sx, sy)
    x1E, y1E = escalaPonto(x1E, y1E, sx, sy)

    pontosEscalados = desenhaReta(x2E, y2E, x1E, y1E)

    return pontosEscalados


