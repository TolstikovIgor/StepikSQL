'''13.1 Функции без параметров
Звездный прямоугольник 1
Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14 \times 1014×10 в соответствии с образцом:
**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********'''
def drow_box():
    for i in range(1):
        print('*' * 10)
    for i in range(12):
        print('*' + ' ' * 8 + '*')
    for i in range(1):
        print('*' * 10)

drow_box()

'''Звездный треугольник 1
Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 1010 в соответствии с образцом:

*
**
***
****
*****
******
*******
********
*********
**********'''
def draw_triangle():
    for i in range(10):
        print('*' * (i+1))

draw_triangle()


'''13.2 Функции с параметрами
Звездный треугольник
Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
fill – символ заполнитель;
base – величина основания равнобедренного треугольника;
а затем выводит его.'''
def draw_triangle(fill, base):
    for i in range(base // 2 + 1):
        for j in range(i + 1):
            print(fill, end='')
        print()
    for k in range(base // 2, 0, -1):
        for l in range(k):
            print(fill, end='')
        print()

fill = input()
base = int(input())

draw_triangle(fill, base)

'''ФИО
Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
name – имя человека;
surname – фамилия человека;
patronymic – отчество человека;
а затем выводит на печать ФИО человека.'''
def print_fio(name, surname, patronymic):
    print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')

name, surname, patronymic = input(), input(), input()

print_fio(name, surname, patronymic)

'''Сумма цифр
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.'''
def print_digit_sum(num):
    sm = 0
    while num != 0:
        sm = sm + num % 10
        num = num // 10
    print(sm)

num = int(input())
print_digit_sum(num)
    

'''13.4 Функции с возвратом значения. Часть 1
Конвертер километров
Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах и возвращает расстояние 
в милях. Формула для преобразования: мили = километры * 0.6214'''
def convert_to_miles(km):
    return (km * 0.6214)

num = int(input())
print(convert_to_miles(num))

'''Количество дней
Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.'''
from datetime import datetime
from calendar import monthrange
def get_days(month):
    current_year = datetime.now().year
    return (monthrange(current_year, month)[1])

num = int(input())
print(get_days(num))

'''Делители 1
Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.'''
def get_factors(num):
    return [i for i in range(1, num+1) if num % i == 0]

n = int(input())
print(get_factors(n))

'''Делители 2
Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.'''
def get_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

def number_of_factors(num):
    return len(get_factors(num))

n = int(input())
print(number_of_factors(n))

'''Найти всех
Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке. Проблема заключается
 том, что данный метод не находит местоположение всех символов а.
Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target и символ symbol и возвращает
 список, содержащий все местоположения этого символа в строке.'''
def find_all(target, symbol):
    return [i for i in range(len(target)) if target[i] in symbol]

s = input()
char = input()

print(find_all(s, char))

'''Merge lists 1
Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию списка, состоящих
 из целых чисел, и объединяет их в один отсортированный список.'''
def merge(list1, list2):
    return sorted(list1 + list2)

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))

'''Merge lists 2
На вход программе подается число nn, а затем nn строк, содержащих целые числа в порядке возрастания. Из данных строк формируются 
списки чисел. Напишите программу, которая объединяет указанные списки в один отсортированный список с помощью функции quick_merge(), 
а затем выводит его.'''
def quick_merge(ln):
    a = []
    for i in range(ln):
        num = [int(c) for c in input().split()]
        a += num
    return a.sort()
n = int(input())
print(*quick_merge(n))


'''13.5 Функции с возвратом значения. Часть 2
Is Valid Triangle?
Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных числа, и возвращает
 значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False в противном случае.'''
def is_valid_triangle(side1, side2, side3):
    arr = sorted([side1, side2, side3])
    return arr[0] + arr[1] > arr[2]

a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))

'''Is a Number Prime? 🌶️
Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True если число 
является простым и False в противном случае.'''
def is_prime(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2

n = int(input())

print(is_prime(n))

'''Next Prime 🌶️🌶️
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число 
большее числа num.'''
def is_prime(num):
    return len([i for i in range(1, num+1) if num % i == 0]) == 2

def get_next_prime(num):
    x = num + 1
    while is_prime(x) == False:
        x += 1
    return x
n = int(input())

print(get_next_prime(n))

'''Good password 🌶️
Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает
 значение True если пароль является надежным и False в противном случае.
Пароль является надежным если:
его длина не менее 88 символов; 
он содержит как минимум одну заглавную букву (верхний регистр); 
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.'''
def is_password_good(password):
    upp = [i for i in password if i.isupper()]
    low = [i for i in password if i.islower()]
    dig = [i for i in password if i.isdigit()]
    return all([len(password) >= 8, upp, low, dig])
txt = input()

print(is_password_good(txt))      

'''Ровно в одном
Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и возвращает 
значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе и False в противном случае.'''
def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))
    
'''Палиндром 🌶️
Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True если указанный
текст является палиндромом и False в противном случае.'''
def is_palindrome(text):
    a = []
    for i in range(len(text)):
        a.extend(text[i])
    x1 = "".join(c for c in a if c.isalpha())
    x2 = x1[::-1]
    if x1 == x2:
        return True
    else:
        return False

txt = input().lower().split()

print(is_palindrome(txt))

'''BEEGEEK
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет
 от математики, то он решил:
число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает
 значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.'''
def is_valid_password(password):
    p = password.split(':')
    a = 0
    for i in range(2, int(p[1]) //2 + 1):
        if int(p[1]) % i == 0:
            a += 1
    return p[0] == p[0][::-1] and a <= 0 and int(p[2]) % 2 == 0 and len(p) == 3

psw = input()

print(is_valid_password(psw))

'''Правильная скобочная последовательность 🌶️
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из символов
 ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной последовательностью и False в 
 противном случае.'''
def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return not text

txt = input()
print(is_correct_bracket(txt))

'''Змеиный регистр
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует
 его в «змеиный регистр».'''
def convert_to_python_case(text):
    t1 = text.lower()
    t2 = t1[0]
    for i in range(1, len(t1)):
        if text[i] == t1[i]:
            t2 = (t2 + t1[i])
        elif text[i] != t1[i]:
            t2 = (t2) + ("_") + (t1[i])
    return t2
txt = input()
print(convert_to_python_case(txt))


'''13.6 Функции с возвратом значения. Часть 3
Середина отрезка
Напишите функцию get_middle_point(x1, y1, x2, y2), которая принимает в качестве аргументов координаты концов отрезка (x_1; \, y_1)(x 
 ) и возвращает координаты точки являющейся серединой данного отрезка.'''
def get_middle_point(x1, y1, x2, y2):
    return ((x1 + x2)/2), ((y1 + y2)/2)

x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)

'''Площадь и длина
Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает два значения: длину 
окружности и площадь круга, ограниченного данной окружностью.'''
def get_circle(radius):
    return (2 * 3.141592653589793 * radius), (3.141592653589793 * radius ** 2)

r = float(input())

length, square = get_circle(r)
print(length, square)

'''Корни уравнения 🌶️🌶️
Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты квадратного уравнения ax^2+bx+c = 0ax 2 +bx+c=0 и возвращает его корни в порядке возрастания.'''
from math import sqrt
def solve(a, b, c):
    D = b**2 - 4*a*c
    l = [((-b + sqrt(D)) / (2 * a)), ((-b - sqrt(D)) / (2 * a))]
    return min(l), max(l)

a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)


