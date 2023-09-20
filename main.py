import math



print('1. Сложить 2 числа ')
print('2. Вычесть первое из второго ')
print('3. Перемножить два числа ')
print('4. Разделить первое на второе')
print('5. Возвести в степень N первое число ')
print('6. Найти квадратный корень из числа   ')
print('7. Найти факториал из числа ')
print('8.Найти синус')
print('9.Найти косинус')
print('10.Найти тангенс')
print('Введите операцию ,которую хотите использовать')



def entry():
    while True:
        try:
            print('Введите первое число')
            b = float(input())
            print('Введите второе число')
            c = float(input())
            return b,c
        except ValueError:
            print('Ошибка ввода. Попробуйте ввести числа.')

def entry1():
    while True:
        try:
            print('Введите первое число')
            b = float(input())
            return b
        except ValueError:
            print('Ошибка ввода. Попробуйте ввести числа.')




a = input("")
if (a=="1"):
    b,c=entry()

    print('Сложение чисел', b+c)
elif a=="2":
    b,c = entry()
    print('Вычитание второго числа из первого', b-c)
elif a=="3":
    b,c=entry()
    print('Умножение чисел:', b * c)
elif a =="4":
   b,c = entry()
   if c == 0:
       print('Вы делите на 0 ,а так нельзя плохая девочка,попробуйте другое число')
   else:
        print('Деление первого на второе', b / c)
elif a=="5":
    b = entry1()
    print('Введите степень в которую хотите возвести')
    c = float(input())
    print(F'Возведение в степень:{b**c}')
elif a == "6":
    b = entry1()
    print('Корень из этого числа:', math.sqrt(b))
elif a == "7":
    while True:
        try:
            number = int(input('Введите число: '))
            if number < 0:
                raise ValueError('Число должно быть положительным')
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i
            print(factorial)
            break
        except ValueError:
            print('Ошибка ввода. Попробуйте ввести числа.')

elif a =="8":

    b = entry1()
    print('синус угла :', math.sin(b))

elif a == "9":
    b = entry1()
    print('косинус угла:', math.cos(b))
elif a == "10":
    b = entry1()
    print('тангенс угла:', math.tan(b))


