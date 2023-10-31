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
import datetime
def counts_time(funk):
    def wraper():
        print('Декоратор заработал')
        start=datetime.datetime.now()
        podnyt=funk()
        finesh=datetime.datetime.now()
        otvet=finesh-start
        print('Декоратор закончил работу')
        return otvet
    return wraper

@counts_time
def a():
    b=input()
    return b

otvet=a()
print(otvet)


