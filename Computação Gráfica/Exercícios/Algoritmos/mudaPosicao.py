from desenhaRetaCG import *
def mudaPonto(x, y, tx, ty):
    x1 = x + tx
    y1 = y + ty
    return x1, y1

def desenhaRetaMudada(x1, y1, x2, y2, tx, ty):
    x2T, y2T = x2, y2
    x1T, y1T = x1, y1
    x2T, y2T = mudaPonto(x2T, y2T, tx, ty)
    x1T, y1T = mudaPonto(x1T, y1T, tx, ty)

    pontosTrans = desenhaReta(x1T, y1T, x2T, y2T)

    return pontosTrans

def calculaPivo(x, y):
    tx = x
    ty = y
    if x > 0:
        tx = -x
    else:
        tx = x

    if y > 0:
        tx = -y
    else:
        ty = y

    return tx, ty

def desenhaRetaPivo(x1P, y1P, x2, y2):
    tx, ty = calculaPivo(x1P, y1P)
    retaMudada = desenhaRetaMudada(x1P, y1P, x2, y2, tx, ty)
    return retaMudada














