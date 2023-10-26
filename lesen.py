# heroes = {
#     'Зелёный парень', 'Человек-таракан', 'Алюминиевый человек',
#     'Уганда', 'Баба-Яга', 'Лариса Романова', 'Зевс', 'Капитан очевидность'
# }
# while True:
#     a=input('Введитеимя героя: ')
#     if a in heroes:
#         print('На месте')
#         print('весь список ваших друзей: ', heroes)
#     else:
#         print('Такого нет')
#         c=input('хотите ли вы его добавить да/нет: ')
#         if c.lower()=='да':
#             heroes.add(a)
#             print('весь список ваших друзей: ', heroes )
#         b = input('хотите продолжть да/нет: ')
#         if b.lower() == 'нет':
#             break



a=input('введите текст: ')

a=a.lower()

punctuashen=[',','.','!','?','-','(',')']

for i in punctuashen:
    a=a.replace(i,'')
m=a.split()
mnojestvo=set(m)
n=len(mnojestvo)
na=m[0]
wa=m[0]
char_frequency = {}
for char in a:
    if char in char_frequency:
        char_frequency[char]+=1
    else:
        char_frequency[char]=1

for l in m:
    if len(l)>len(na):
        na=l
    elif len(l)<len(wa):
        wa=l
print('Количество разных слов:', n)
print("Самое длинное слово:", na)
print("Самое короткое слово:",wa )

print("Частота символов:")

for char, frequency in char_frequency.items():
    print(f"{char}: {frequency}")

