def bhaskara(a, b, c):
    delta = (b ** 2) - 4 * a * c

    saida = ''

    if a == 0:
        saida = "O valor de a, deve ser diferente de 0"
    elif delta < 0:
        saida = "Sem raízes reais"
    elif delta == 0:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        saida = "x1: {}".format(x1)
    else:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)

        saida = "x1: {}, x2: {}".format(x1, x2)

    return saida
