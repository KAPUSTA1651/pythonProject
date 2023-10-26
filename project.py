# class Person:
#     def __init__(self, name, hair, oko, rost):
#         self.name = name
#         self.hair = hair
#         self.oko = oko
#         self.rost = rost
#         self.get_name()
#     def get_name(self):
#         print(f'Его зовут {self.name}!')
#         print(f'У него {self.hair} цвет волос')
#
#
# class Animal:
#     def __init__(self, name, hair, oko, rost):
#         self.owner = Person(name, hair, oko, rost)
#
#
#
# anikm=Animal(name=input('Как зовут владельца?: '), hair=input('как у него цвет волос?: '), oko=input('какой у него цвет глаз?: '), rost=input('какой у него рост?: '))
#



class Transport:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

class  Airplane(Transport):
    def __init__(self, speed, color):
        super().__init__(speed, color)
    def fly(self):
        print(f'{self.color} самолет летит со скорость {self.speed} км/ч')

