class Animal:

    @staticmethod
    def eat():
        print("Animal eats")


class Rabbit(Animal):  # child class
    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()
rabbit.eat()