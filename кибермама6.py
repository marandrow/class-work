#1
m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']

m.remove(0.25)
m.remove(15)
m.remove('10')
print(m)

#2

abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

del abc[1:5]
print(abc)

#3

numbers = [1, 4]

numbers.insert(1, '2')
numbers.insert(2, '3')
print(numbers)

#4

mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]

mass.remove(-6)
mass.remove(-20)
mass.remove(-6)
mass.remove(-4)

mass.sort(reverse=True)
print(mass)
mass.sort(reverse=False)
print(mass)

#5

a = int(input('Введите колличнство вводов: '))
spisok_minus = []
spisok_plus = []
spisok = []
count = 0

while count < a:
    b = int(input('Введите число: '))
    count += 1
    if b < 0:
        spisok_minus.append(b)
    elif b > 0:
        spisok_plus.append(b)
    else:
        spisok.append(b)

c = len(spisok)
spisok.clear()
for i in range (c):
    spisok.append('*')

print(sum(spisok_minus), sum(spisok_plus)/len(spisok_plus), 'Колличество звёзд: ', c, spisok)
