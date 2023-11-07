# def my_ferst_decorator(funk):
#     def wraper():
#         print('Декоратор заработал')
#         podnyt=funk()
#         otvet=podnyt.upper()
#         print('Декоратор закончил работу')
#         return otvet
#     return wraper
#
# @my_ferst_decorator
# def a():
#     b=input()
#     return b
#
# otvet=a()
# print(otvet)
#
# import datetime
# def counts_time(funk):
#     def wraper():
#         print('Декоратор заработал')
#         start=datetime.datetime.now()
#         podnyt=funk()
#         finesh=datetime.datetime.now()
#         otvet=finesh-start
#         print(otvet)
#         print('Декоратор закончил работу')
#         return otvet
#     return wraper
#
# # @counts_time
# # def a():
# #     b=input()
# #     return b
# #
# # otvet=a()
# # print(otvet)
# #
# #
#
# # дано натуральное число x вычисли: 1+2+3+...x
# # если ввели число 3 то выведет 6
# @counts_time
# def a():
#     x=100
#     n=0
#     for i in range(1, x+1):
#        n+=i
#     print(n)
#
# a()
# @counts_time
# def uno():
#     x=1000
#     n=0
#     for i in range(1, x+1):
#        n*=i
#     print(n)
#
# uno()
#
# # дано натурально число, вычесли (1**1)+(2**2)+(3**3)+...+(x**x)
#
# @counts_time
# def stepan():
#     n=100
#     x=0
#     for i in range(1,n+1):
#         v=i**i
#         x+=v
#     print(x)
# stepan()
#
# # дано натуральн число x вычесли: (1**1)/(2**2)*(3**3)/...*(х**х)
# @counts_time
# def vasy():
#     n=100
#     l=1
#     for i in range(1,n+1):
#         m=i**i
#         if i%2==0:
#             b=l*m
#             l+=b
#         else:
#             b=l/m
#             l+=b
#     print(l)
#
# vasy()