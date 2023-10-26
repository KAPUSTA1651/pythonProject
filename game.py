# import os
#
# clear = lambda: os.system('cls')
#
#
# print('Привет! Я загадал слово и твоя задача-угадать его по буквам')
# input('*Нажмите Enter, чтобы продолжить')
# clear()
# print('Поехали! ')
#
# word='черепаха'
# letters=[]
# isWin=True
# hp=10
# while hp>0:
#     letter=input('Введите букву: ')
#     letters.append(letter)
#     print(letters)
#     for symb in word:
#         if symb in letters:
#             print(symb, end=' ')
#         else:
#             print('*',end=' ')
#     print()



# def generate_password(number=6):
#     n=[]
#     for i in range(number):
#         x=random.randint(1,3)
#         if x==1:
#             n.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
#         elif x==2:
#             n.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
#         elif x==3:
#             n.append(random.choice('0123456789'))
#     m=''
#     for a in n:
#         m+=a
#     return m
#print(generate_password())