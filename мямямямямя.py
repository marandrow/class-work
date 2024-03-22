#1
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if num1 > num2:
    print("Наибольшее число:", num1)
else:
    print("Наибольшее число:", num2)
#2
a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("YES")
else:
    print("NO")
#3
year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")

