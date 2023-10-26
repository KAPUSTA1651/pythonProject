# a=int(input('первый чел: '))
# b=int(input())
# c=int(input())
# n=int(input('второй чел: '))
# g=int(input())
# y=int(input())
# f=a+b+c
# v=n+g+y
# if f>v:
#     print('второй чел старше')
# elif f<v:
#     print('первый чел старше')
# else:
#     print('у них одинаковый год рождения')
# #
# a=int(input())
# b=int(input())
# c=int(input())
# if a==b==c:
#     print(3)
# elif a==b or b==c or a==c:
#     print(2)
# else:
#     print(0)

# y = int(input())
# if (y % 4 == 0 and y%100 != 0) or (y%400 == 0):
#     print("1")
# else:
#     print("0")

# a=int(input())
# b=int(input())
# c=int(input())
# h=max(a, b, c)
# print(h)

# a=int(input())
# v=a//100
# j=a//10%10
# g = a % 10
# s=0
# if v%2==0:
#     s+=1
# if j%2==0:
#     s+=1
# if g % 2 == 0:
#     s+=1
# print(s)







# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# if a==b==c:
#     print(d)
# elif a==c==d:
#     print(b)
# elif a==b==d:
#     print(c)
# else:
#     print(a)

# a=int(input())
# b=int(input())
# c=int(input())
# if a==b==c:
#     print(3)
# elif a==c:
#     print(2)
# elif b==c:
#     print(2)
# elif a==b:
#     print(2)
# else:
#     print('ни шиша')

#a=int(input()) #Дано 44-ех значное целое число numnum. Возведи каждую цифру этого числа в квадрат и соедини результаты в одно число.
# v=(a//1000)**2
# h=(a//100%10)**2
# j=(a//10%10)**2
# g=(a%10)**2
# print(str(v)+str(h)+str(j)+str(g))




# n=input()
# k=n[1:4]
# l=n[4:7]
# y=n[7:9]
# g=n[9:11]
# print(str('+7'),str('(')+k+str(')'),l+str('-')+y+str('-')+g)


#
# a=int(input()) Даны два целых числа aa и bb, причём a ≤ ba≤b. Выведи все числа в диапазоне от aa до bb включительно.
# b=int(input())
# for i in range(a, b+1):
#     print(i)

# a=int(input())
# h=0
# for i in range(a+1):
#     h=h+i
#     print(h)

# a = int(input())
# h = 1
# for i in range(a+1):
#     l=(h+i)**h
#     j=(h-i)**h
# print(h)


# a=int(input())
# h=0
# for i in range(1, a+1):
#     if i%2==0:
#         h = h - i ** i
#     else:
#         h=h+i**i
# print(h)

# a=int(input())  #факториал
# h=1
# k=0
# for i in range(1, a+1):
#     h=h*i
#     #k=h+k
# print(h)


# Даны два целых числа aa и bb, причём a ≤ ba≤b. Выведи все числа в диапазоне от aa до bb включительно.
# a=int(input())
# b=int(input())
# while a<=b:
#     print(a)
#     a=a+1

#
# Дано натуральное число NN. Вычисли:
#
# 1 + 2 + 3 + ... + N1+2+3+...+N.
# n = int(input())
# h=0
# j=0
# while h<n:
#     h=h+1
#     j=j+h
#     print(j)

# a=int(input())    Дано натуральное число NN. Выведи все степени числа 22, не превосходящие NN.
# h=1
# while h<a:
#     print(h)
#     h=h*2
#
# a=int(input())  Даны натуральные числа AA и BB. Используя только операции ++ и -−, следует определить и вывести частное от деления AA на BB нацело и остаток от данного деления.
# b=int(input())
# h=0
# while a>b:
#     a=a-b
#     h+=1
# print(h, a)

# a = int(input())     #Дано натуральное число NN. Используя операции //// и \%%, следует перевернуть данное число.
# while a!=0:
#     b=a%10
#     a=a//10
#     print(b, end='')

# a=int(input())
# if a%2==0 and a%a==0:
#     print(0)
# else:
#     print(1)

# a=int(input())
# f1=1
# f2=1
# h=0
# print(1)
# while f1<a:
#     print(f2)
#     h= f1 + f2
#     f1=f2
#     f2=h


# a=1
# while a<=10:
#     print(a**2)
#     a+=1

# a = int(input())
# b = int(input())
# for i in range(1,a+1):
#     i**b
#     print(i)

# a='hello'
# b=list(a)
# f=b[0]
# print(f)


# a=[]
# for i in range(3):   Создай список, состоящий из 33-х элементов, которые указываются функцией ввода данных. Выведи первый и последний элементы.
#     a.append(input('введите значение: '))
# print(a[0],a[-1])

# f=[]
# h=0
# for i in range(4):
#     a=int(input())
#     f.append(a)
#     h+=a
# j=h/4
# print(int(j))

# deals = [
# 'погулять с друзьями',
# 'почитать новости и сцепиться с кем-нибудь в комментах',
# 'почитать книжку',
# 'рассмотреть потолок',
# 'поиграть в Brawl stars',
# 'помыть посуду',
# 'сказать родителям, что заболел',
# 'залипнуть в летсплеях по роблоксу'
# ]
# index=int(input('введите индекс который хотите заменить: '))
# deals[index]=input('введите дело которое хотите вставить: ')
#
# print(deals)

# m = [
# 'январь', 'февраль', 'март', 'апрель',
# 'май', 'июнь', 'июль', 'август',
# 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
# ]
# winter = m[-1], m[0], m[1]
# spring = m[2:5]
# summer=m[5:8]
# autumn=m[8:11]
# print('Зима: ', list(winter))
# print('Весна: ', spring)
# print('лето: ', summer)
# print('осень: ', autumn)

# items = []
# a=1
# while a!='':
#   a=input('введите покупку: ')
#   if a!='':
#     items.append(a)
# print(items)

# d = [
#     'погулять с друзьями',
#     'почитать новости и сцепиться с кем-нибудь в комментах',
#     'почитать книжку',
#     'рассмотреть потолок',
#     'поиграть в Brawl stars',
#     'помыть посуду',
#     'сказать родителям, что заболел',
#     'залипнуть в летсплеях по роблоксу',
#     'покормить кота'
#     ]
# for i in d:
#     n=input(i+'  -дело сделано введите: да/нет')
#     if n=='да':
#         print(i,'- сделано')
#     elif n=='нет':
#         print(i,'- не сделано')



# n=[]
# a=1
# while a!='':
#   a=input()
#   if a!='':
#     n.append(a)
# print(n)
# print(max(n))


# book_phones = {
#     'Квам-Дамн': '-79899899889',
#     'Лук Скамворкер': '112',
#     'Петард Вейпер': '1',
#     'Лия Моргала': '+09998765432',
#     'Эдуард Скамворкер': '0',
# }
# names=input('введите имя: ')
# if names in book_phones:
#     print(book_phones[names])
# else:
#     print('Нет в телефонной книге')


# book_phones = {
#     'Квам-Дамн': '-79899899889',
#     'Лук Скамворкер': '112',
#     'Петард Вейпер': '1',
#     'Лия Моргала': '+09998765432',
#     'Эдуард Скамворкер': '0'
# }
#
# name=input('введите имя: ')
# h=input('введите номер телефона: ')
# if name !='' and h!='':
#     book_phones[name]=h
#     for key in book_phones:
#         print(f'{key}: {book_phones[key]}')
# elif name !='' and name in book_phones:
#     book_phones[name]=h
#     for key in book_phones:
#         print(f'{key}: {book_phones[key]}')
# else:
#     print('Нет в телефонной книге')




# book_phones = {
#   'Квам-Дамн': '-79899899889',
#   'Лук Скамворкер': '112',
#   'Петард Вейпер': '1',
#   'Лия Моргала': '+09998765432',
#   'Эдуард Скамворкер': '0'
# }
# n=int(input('Введите  1 — показать, 2 — добавить, 3 — изменить, 4 — удалить : '))
# if n==1:
#     name=input('введите имя: ')
#     if name in book_phones:
#         print(book_phones[name])
#     else:
#         print('Нет в телефонной книге')
# elif n==2:
#     name=input('введите имя: ')
#     t=input('введите номер телефона')
#     book_phones[name]=t
#     for key in book_phones:
#         print(f'{key}: {book_phones[key]}')
# elif n==3:
#     name=input('введите имя: ')
#     t=input('введите номер телефона')
#     book_phones[name]=t
#     for key in book_phones:
#         print(f'{key}: {book_phones[key]}')
# elif n==4:
#     name=input('введите имя: ')
#     book_phones.pop(name)
#     for key in book_phones:
#         print(f'{key}: {book_phones[key]}')
#         #print(key, ':', book_phones[key])


book_phones = {
  'Квам-Дамн': '-79899899889',
  'Лук Скамворкер': '112',
  'Петард Вейпер': '1',
  'Лия Моргала': '+09998765432',
  'Эдуард Скамворкер': '0'
}
for i in book_phones