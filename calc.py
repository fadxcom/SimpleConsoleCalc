def DoArifOperation(x,y,z):
    if z == '+':
        return x + y
    elif z == '-':
        return x - y
    elif z == '*':
        return x * y
    elif z == '/':
        return x / y
def CheckVariable(var):
    try:
        return int(var)
    except ValueError:
        print('Ошибка!!! В поле ввода должно быть число.')
def ShowErrore():
    print('Ошибка!!! Проверьте ввод.')

while True:
    while True:
        a = input('Введите первое число: ')
        a = CheckVariable(a)
        if type(a) is int:
            break
        else:
            ShowErrore()
    while True:
        b = input('Введите вротое число: ')
        b = CheckVariable(b)
        if type(b) is int:
            break
        else:
            ShowErrore()
    while True:
        c = input('Введите арифметическую операцию (+,-,*,/): ')
        if c == '+' or c == '-' or c == '*' or c == '/':
            if c == '/' and b == 0:
                print('На ноль делить нельзя. Используйте друю операцию.')
            else:
                break
        else:
            ShowErrore()
    return_arif = DoArifOperation(a,b,c)
    print('Ответ:',return_arif)
