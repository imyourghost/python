# 1. Написать класс, который выводит сумму купленных продуктов
# Продукты (у каждого есть цена)
# на вес, на штуки, на объем
# 2. Написать размерность вычислений 300$ за 4000кг
# 3. Сделать скидку 5% при покупке двух товаров поштучно
# 4. При покупке за граммы округлять до 50г\


class Produkts (object):
    def __init__(self, name, price, kol):
        self.price_val = 'руб '
        self.val = 'шт.'
        self.name = name
        self.price = price
        self.kol = kol

    def total_price(self, price):
        self.tp = self.price * self.kol
        print(self.name, self.tp, self.price_val, 'за', self.kol, self.val)


class Ves(Produkts):
    def total_price(self, price):
        self.val = 'КГ'
        self.tp = super().total_price(self.price)


class Objom(Produkts):
    def total_price(self, price):
        self.val = 'литра(ов)'
        self.tp = super().total_price(self.price)


class Shtuk(Produkts):

    def total_price(self, price):
        if self.kol > 2:
            self.tp = self.price * 0.95 * self.kol
        else:
            self.tp = self.price * self.kol
        print(self.name, self.tp, self.price_val, 'за', self.kol, self.val)

morkva = Ves('morkva -', 54, 2000)
kartofel = Shtuk('kartofel -', 20, 4)
pivas = Objom('pivas -', 150, 2)

morkva.total_price(morkva)
kartofel.total_price(kartofel)
pivas.total_price(pivas)
