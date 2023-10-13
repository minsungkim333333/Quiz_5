class fishbread:
    def __init__(self, inside, price):
        self.inside = inside
        self.price= price
        self.total = 0
    def sell(self):
        print(self.inside + "이 " + str(self.price) + "원에 판매되었습니다.")
        self.total=self.total + self.price
    def eat(self):
        print(self.inside + "을 먹었습니다.")

my_fishbread= fishbread("슈크림 붕어빵", 1000)
my_fishbread.sell()
my_fishbread.sell()
my_fishbread.sell()
print(my_fishbread.total)
my_fishbread.eat()
your_fishbread= fishbread("팥 붕어빵", 600)
your_fishbread.sell()
your_fishbread.sell()
your_fishbread.sell()
your_fishbread.sell()
your_fishbread.sell()
print(your_fishbread.total)
your_fishbread.eat()
