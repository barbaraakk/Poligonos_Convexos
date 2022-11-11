import math


class Ponto:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return (f"Área atual do polígono {self.x} - Perímetro atual do polígono: {self.y}. ")


class Poligono:

    def __init__(self):
        self.pontos = []

    def area(self):
        total = 0
        n = len(self.pontos)
        for i in range(n):
            x0 = self.pontos[i].x
            y0 = self.pontos[i].y
            x1 = self.pontos[(i+1) % n].x
            y1 = self.pontos[(i+1) % n].y

            total += (x0 * y1 - x1 * y0)

        return total/2

    def perimetro(self):
        p = 0
        n = len(self.pontos)
        for i in range(n):
            x1 = self.pontos[(i+1) % n].x
            y1 = self.pontos[(i+1) % n].y
            x0 = self.pontos[i % n].x
            y0 = self.pontos[i % n].y

            p += math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

        return p

    def addPonto(self, ponto):
        self.pontos.append(ponto)

    def __str__(self):
        return (f"Área do polígono: {self.area()} - Perímetro do poligono: {self.perimetro()}")


def main(x, y):
    ponto = Ponto(x, y)
    poligono.addPonto(ponto)
    return poligono.__str__()


poligono = Poligono()
while True:
    x = input("ponto X: ")
    if x == '':
        break
    y = float(input("ponto Y: "))
    print(main(x, y))
