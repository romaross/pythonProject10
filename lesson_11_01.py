""" 1 Переопределить методы change_weight, change_height в классе Parrot. В
случае не передачи параметра - вес изменяется на 0.05 """

'''Добавить метод jump, принимающий высоту прыжка. Метод
выводит сообщение “Jump X meters” Переопределить метод
jump в дочерних классах. Если передать методу jump класса
dog значение больше 0.5, выводить сообщение “Dogs cannot
jump so high, аналогично для кошек(2), для попугаев(0.05)'''

''''' 3 Добавить в класс Parrot новый атрибут - species (порода)'''''

'''Добавить в класс Pet пустой метод voice. Заменить
имена методов bark, meow на voice. Добавить voice
для класса Parrot.
Создать функцию, принимающая список животных и
вызывающая у каждого животного метод voice. '''


class Pat:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def jump(self, x):
        print(f'Jump {x} meters')

    def voice(self):
        pass

    def change_weight(self, weight=0.1):
        self.__weight = weight

    def change_height(self, height=0.2):
        self.__height = height


class Parrot(Pat):
    def __init__(self, name, age, weight, height, species=None):
        super().__init__(name, age, weight, height)
        self.species = species

    def change_weight(self, weight=0.05):
        self.__weight = weight

    def change_height(self, height=0.05):
        self.__height = height

    def jump(self, x):
        if x >= 0.05:
            print('Parrot cannot jump that high')
        else:
            super().jump(x)

    def voice(self):
        print('co co co')


parrot = Parrot(name='Gosha', age=4, weight=0.5, height=0.2, species='cockatoo')
parrot.jump(0.03)
print(parrot.species)
parrot.voice()


class Cat(Pat):
    # def change_weight(self, weight=0.05):
    #     self.__weight = weight
    #
    # def change_height(self, height=0.05):
    #     self.__height = height

    def voice(self):
        print('Meeoow')

    def jump(self, x):
        if x >= 0.2:
            print('Cat cannot jump that high')
        else:
            super().jump(x)


cat = Cat(name='Felix', age=7, weight=2, height=0.4)
cat.jump(0.1)
cat.voice()


class Dog(Pat):

    def voice(self):
        print('Woof Woof')

    def jump(self, x):
        if x >= 0.5:
            print('Dog cannot jump that high')
        else:
            super().jump(x)


dog = Dog(name='Sharik', age=3, weight=5, height=0.5)
dog.jump(0.4)
dog.voice()


def list_of_animals():
    animals = [cat, dog, parrot]
    for animal in animals:
        animal.voice()


list_of_animals()
