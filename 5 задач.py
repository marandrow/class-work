#1 задание
a = int(input())
x = int(input())
print(max(a,x), min(a,x))
#2 задание
a = int(input("введите сторону квадрата:"))
R = int(input("введите радиус круга:"))
if a > R * 2:
    print("Впишется")
else:
    print("Не впишется")
#3 задача
x = int(input("Введите y:"))
if y < 0:
    y = x ** 2
else:
    y = 1 / x ** 2 
print (y)
#4 задача
a = int(input("введите сторону квадрата:"))
R = int(input("введите радиус круга:"))
d = a * 2 * 0.5
R2 = R * R2
if d > R2:
    print("Впишется")
else:
    print("не впишется")
#5 задача 
a = int(input("Введите первое число"))
b = int(input("введите второе число"))
    print(max(a,b), min(a,b))