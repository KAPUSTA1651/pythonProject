#import antigravity
#import this



# book_phones = {
#     'Квам-Дамн': '-79899899889',
#     'Лук Скамворкер': '112',
#     'Петард Вейпер': '1',
#     'Лия Моргала': '+09998765432',
#     'Эдуард Скамворкер': '0'
# }
# n=int(input('введите номер действия: 1 — Показать, 2 — Добавить, 3 — Изменить, 4 — Удалить, 5 — Показать все имена в книге, 6 — Показать все номера в книге:  '))
# if n==1:
#     n=input('введите имя: ')
#     n in book_phones
#     print(book_phones[n])
# elif n==2:
#     n = input('введите имя: ')
#     j=input('введити номер телефона: ')
#     book_phones[n]=j
#     print(book_phones)
# elif n==3:
#     n = input('введите имя: ')
#     j=input('введити номер телефона: ')
#     book_phones[n]=j
#     print(book_phones)
# elif n==4:
#     y = input('введите имя: ')
#     del book_phones[y]
#     print(book_phones)
# elif n==5:
#     f =  book_phones.keys()
#     for i in f:
#         print(i)
# elif n==6:
#     f = book_phones.values()
#     for i in f:
#         print(i)
# else:
#     print('Такого действия нет')



# book_phones = {
#   'Квам-Дамн': '-79899899889',
#   'Лук Скамворкер': '112',
#   'Петард Вейпер': '1',
#   'Лия Моргала': '+09998765432',
#   'Эдуард Скамворкер': '0'
# }
# for key in book_phones.items():
#     print(key)
#print("('""{0}', '{1}""')".format(key,value))



# months = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
# 'Декабрь')
#
# winter = months[-1:] + months[0:2]
# spring = months[2:5]
# summer = months[5:8]
# autumn = months[8:11]
# half_year1=winter,spring
# half_year2=summer,autumn
# print(*winter)
# print(half_year1, half_year2)




# a=int(input('Введите температуру по Цельсию: '))
# def c():
#     print(1.8*a+32)
# c()


# def multiply_range(start, end):
#     h=1
#     if start>end:
#         start, end= end, start
#     for i in range(start, end+1):
#         h = i*h
#     return h
# a = multiply_range(int(input()), int(input()))
# print(a)




#
# def sum_num(n, b):
#   try:
#       return float(n) + float(b)
#   except:
#       print( "Функция сложения работает только с числами.")
#       return 0
#
# def sub_nums(n, b):
#   try:
#       return float(n) - float(b)
#   except:
#       print( "Функция вычитания работает только с числами.")
#       return 0
#
#
# def multiply_nums(n, b):
#   try:
#         return float(n) *  float(b)
#   except:
#       print( "Функция умножения работает только с числами.")
#       return 0
#
# def divide_nums(n, b):
#   try:
#       return float(n) / float(b)
#   except ZeroDivisionError:
#       print("Нельзя делить на ноль.")
#       return 0
#   except:
#       print("Функция деления работает только с числами.")
#       return 0
#
#
# print('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление')
# choice = input('Введите номер действия: ')
# if choice=='1':
#     print(sum_nums(str(input()),str(input())))
#
# elif choice=='2':
#     sub_nums(str(input()),str(input()))
# elif choice=='3':
#     multiply_nums(str(input()),str(input()))
# elif choice=='4':
#     divide_nums(str(input()),str(input()))
# else:
#     print("Такого действия нет.")
#
#
#
# print('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n10. Выход')
# while True:
#     choice = input('Введите номер действия: ')
#     if choice in {'1', '2', '3', '4', '10'}:
#         if choice != '10':
#             num1=input('Введите первое число: ')
#             num2=input('Введите второе число: ')
#             if choice=='1':
#                 print(num1, "+", num2, "=", sum_num(num1, num2))
#             if choice=='2':
#                 print(num1, "-", num2, "=", sub_nums(num1, num2))
#             if choice=='3':
#                 print(num1, "*", num2, "=", multiply_nums(num1, num2))
#             if choice=='4':
#                 print(num1, "/", num2, "=", divide_nums(num1, num2))
#         else:
#             print('Выход из калькулятора')
#             break
#     else:
#         print('Такого действия нет.')



#
# def sum(**name):
#     print(name)
# sum(name1='рома',name2='иван',name3='вова',name4='гена')

# def n():
#     print('hi')
#     print('hello')
# n()
# n()


# a=int(input())
# b=str(input())
# if b=='f':
#     c=(a-32)*(5/9)
#     print(c,'c')
# elif b=='c':
#     c=a*(5/9)+32
#     print(c,'f')

# def add(a,b):
#     sum = float(a) + float(b)
#     print(int(sum))
#
# add(-144, 12**2)

# def recursion(n):
#     print(n)
#     if n == 1:
#         return 1
#
#     return recursion(n - 1)
#
#
# recursion(int(input('Число: ')))


# def anfh(n=int(input())):
#     if(n % 2 == 0):
#         print('Even')
#     else:
#         print('Odd')
#     return
#
#
# anfh()


# def a(s=input()):  Создай функцию, которая принимает аргументом строку и выводит на экран обратную ей. Используй тайп-хинтинг.
#     return s[::-1]
# print(a())
#
# a()

# def n(s=input()):
#     print(s.replace('1','!'))
# n()


#
# import math
#
# def get_sum(*end):
#     s=sum(end)
#     return s
# print(get_sum(1,0, math.inf))


# def f(a=int(input()),b=str(input())):
#     if b=='f':
#         c=(a-32)*(5/9)
#         print(c,)
#     elif b=='c':
#         c=(9/5)*a+32
#         print(c,)
# f()

# def a(b=float(input())):
#     n=b**2
#     return n
#
# print(a())


# def dnk(a=input()):
#     c=a.count('A')
#     c1=a.count('T')
#     c2=a.count('C')
#     c3=a.count('G')
#     print(c, c1, c2, c3)
# dnk()

# def rnk(a=input()):
#     n=a.replace('T','U')
#     print(n)
# rnk()


# def m(a:str,b:int) ->int:
#     return a*b
# print(m('Рома',10))


# def dnk(a=str(input())):
#   h=len(a)
#   c = a.count('C')
#   c1=a.count('G')
#   n=c+c1
#   m=(n/h)*100
#   print(m)
# dnk()

# strings = ["как", "дела", "дела", "как", "как", "у тебя", "дела", "как", ":-O"]
# m=set(strings)
# print(sorted(m))


# white_list = set()
# answers = set()
#
# w=1
# request = 1
#
# while w:
#    w=input('введите разрешонный запрос: ')
#    if w!='':
#     white_list.add(w)
# while request:
#     request=input('введите запрос: ')
#     if request!='':
#         answers.add(request)
# print(*white_list.intersection(answers))



# def slovar(a):
#     n={}
#     for i in a:
#         if i not in n:
#             n[i]=1
#         else:
#             n[i]+=1
#     return n
#
# print(slovar(input()))
n={}

# def info(filename):
#     try:
#         with open(filename,  "r", encoding='utf-8') as f:
#             text = f.read()
#             print(text)
#
#     except FileNotFoundError:
#         print("Файл не найден")
#
# info('text.txt')

# def abc(a):
#     n=''
#     pare={"A": 'T',
#           "T": "A",
#           "C": "G",
#           "G": "C"
#           }
#     for i in a:
#         n+=pare[i]
#     return n
#
# print(abc(input()))


# class  Airplane:
#     engines=input()
#     seats=input()
#
#
# plane=Airplane()
# print(plane.engines)
# print(plane.seats)


# import qrcode
#
# data = 'Hello, Roman!'
#
# qr = qrcode.QRCode(version=5, box_size=15, border=10)
#
# qr.add_data(data)
#
# img = qr.make_image()
#
# img.save('test.png')
#

# class Car:
#     def __init__(self, color,brend,speed):
#         self.color=color
#         self.brend=brend
#         self.speed=speed
#         print('Автомобиль готов!')
#
# audi = Car('белый','ауди','300')
# nissan = Car('чёрный','ниссан','350')
# bmw = Car('синий','бмв','300')

# class Cat:
#     def __init__(self, name, breed,character,coat_color):
#         print('Котик родился!')
#         self.name=name
#         self.breed=breed
#         self.coat_color=coat_color
#         self.character=character
#         print('Теперь его зовут', name+'!')
#
# cat1 = Cat(name='Вездепух', breed='Мейн-кун', coat_color='рыжий', character='ласковый')
# cat2 = Cat(name='Граф Кусь', breed='Британский короткошёрстный', coat_color='тёмный', character='вредный')


# class Ship:
#     def __init__(self, name, people):
#         self.name=name
#         self.people=people
#     def go_swimming(self):
#         print(f"{self.name} отправился в плаванье")
#     def how_many_people(self):
#         print(f"На борту корабля '{self.name}' находится {self.people} человек.")
#     def stop_ship(self, time):
#         print(f"Корабль '{self.name}' кинул якорь на {time} часов.")
#
# ship= Ship(name='вольный', people=150)
# ship.go_swimming()
# ship.how_many_people()
# ship.stop_ship(time=5)

#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         print(f'Его зовут {self.name}!')
#
# class Cat(Animal):
#     def __init__(self, name):
#         Animal.__init__(self,name)
#         self.get_name()
#
#
# Cat(input('Как его зовут?:'))


# class Auto:
#     def __init__(self, wheel):
#         self.wheel=wheel
#     def hy(self):
#         print(f'В этом авто {self.wheel} колеса')
#     def collor(self, color):
#         print(f'Эта машина {color} цвета')
#
# auto=Auto(wheel=4)
# auto.hy()
# auto.collor(color='чёрный')

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         print(f'Его зовут {self.name}!')
#
# class Cat(Animal):
#     def __init__(self, name):
#         Animal.__init__(self, name)
#         self.get_name()
#
# class Lion(Cat):
#     def __int__(self, name):
#         Cat.__init__(self, name)
#
#     def play_game(self):
#             print(f"{self.name} играет с едой.")
#
#
# anim=Lion(input())
# anim.play_game()

# Вместо ... нужно дописать код

# Это класс работы с инвентарём.
# Его задача - хранить предметы и предоставлять методы для взаимодействия с ними.
# А именно, добавление и удаление предмета, сортировка всех предметов по алфавиту и демонстрация всех предметов рюкзака.
class Inventory:
    def __init__(self, *items):
        self.__items = list(items)

    # Сортирует инвентарь по алфавиту
    def sort_iventory(self):
        self.__items = sorted(self.__items)

    # Добавляет предмет в инвентарь
    def add_item(self, items):
        self.__items.append(items)
        print(f"Добавил {items} в инвентарь")

    # Удаляет предмет из инвентаря
    def remove_item(self, items):
        self.__items.remove(items)
        print(f"Вынул {items} из инвентаря")

    # Показывает весь инвентарь
    def show_items(self):
        print(f'В инвентаре такие предметы: ')
        for i in range(len(self.__items)):
            print(f"{i}. {self.__items[i]}")
#
# ivent=Inventory()


# Вместо ... нужно дописать код

# Это класс работы с инвентарём.
# Его задача - хранить предметы и предоставлять методы для взаимодействия с ними.
# А именно, добавление и удаление предмета, сортировка всех предметов по алфавиту и демонстрация всех предметов рюкзака.
