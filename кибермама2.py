#1
a = int(input())
b = a // 60
c = a - b * 60
print(b, "часы", c, 'минуты')

#2
print ("Сколько вы спите?")
h = int(input())
a = 8
b = 10
if h==8:
    print ("Это нормально")
elif h>=10:
    print("Пересып")
elif h<=8:
    print("Недосып")

#3
a = int(input())
b = int(input())
c = int(input())
p = (a+b+c)//2
print (int((p*(p-a)*(p-b)*(p-c))**0.5))

#4
a = input("Какой у вас тип фигуры комнаты?")
if a == "Круг":
    r = int(input("введите  значение радиуса"))
    A = 3.14 * r
    print (A)
elif a == "Квадрат":
    b = int(input("введите значение стороны"))
    S = b**2
    print (S)
elif a == "Треугольник":
    h = int(input("Введите значение высоты"))
    d = int(input("ведите значение основания"))
    D = 0.5*h*d
    print(D)

#5
a = int(input("Сколько программистов?"))
b = a % 10
c = a % 100
if b == 1 and c != 11 and c != 12 and c != 13 and c!= 14:
    print (a, "программист")
elif b < 5 and b != 0 and b != 1:
    print (a, "программиста")
else:
    print (a, "программистов")

#6

a = int(input())
a1 = a/100000
a2 = float(a/100000- a1)* 10
a3 = (float(a/10000) - int(a/10000))* 10
a4 = (float(a/1000) - int(a/1000))*10
a5 = (float(a/100)-int(a/100))*10
a6 = (float(a/10)-int(a/10))*10
if (a1 + a2 + a3) == (a4 + a5 + a6):
    print('Счастливый')
else:
    print('Обычный')
