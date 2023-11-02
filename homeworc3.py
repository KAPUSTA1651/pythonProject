# from colorama import init
# init()
# from colorama import Fore, Back, Style
#
#
# a=float(input(Fore.BLUE+ "введите число: "+Style.RESET_ALL))
# b=input(Fore.CYAN+"едите + - * /: ** % ")
# c=float(input(Fore.BLUE+ "введите второе число: "+Style.RESET_ALL))
# if b=="+":
#     x=a+c
#     print(Fore.BLACK , Back.GREEN , "ответ: ", x, Style.RESET_ALL)
# elif b=="-":
#     x=a-c
#     print(Fore.BLACK , Back.GREEN , "ответ: ", x, Style.RESET_ALL)
# elif b=="*":
#     x = a * c
#     print(Fore.BLACK,Back.GREEN, "ответ: ", x, Style.RESET_ALL)
# elif b=="/":
#     if c==0:
#         print(Fore.BLACK+Back.RED+"делить на ноль нельзя!!!"+Style.RESET_ALL)
#     else:
#         x = a / c
#         print(Fore.BLACK,Back.GREEN, "ответ: ", x, Style.RESET_ALL)
# elif b=="**":
#     x=a**c
#     print(Fore.BLACK,Back.GREEN,"ответ", x, Style.RESET_ALL )
# elif b=="%":
#     x=a%c
#     print(Fore.BLACK,Back.GREEN,"ответ", x, Style.RESET_ALL )
#
# else:
#     print(Fore.BLACK+Back.RED+"ошибка вы ввели неверный знак"+Style.RESET_ALL)
# #
# a=input('введите пороль: ')
# if len(a) >= 8 and not a.isupper() and not a.islower() and not a.isalpha() and not a.isdigit():
#     print('сложный')
# elif len(a) >= 8 and a.islower() and not a.isalpha():
#     print('средний')
# elif len(a) >= 8 and (a.isalpha() or a.isdigit()):
#     print('слабый')
# else:
#     print('очень слабый')


def x():
    a=int(input())
    if a>25 and a%2==0:
        print(1)
    else:
        print(0)
        return
x()
