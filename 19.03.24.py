#1
def triangle(x1, y1, x2, y2, x3, y3):
    a = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)
    return a

x1, y1 = map(float, input("Введите координаты вершины A через пробел: ").split())
x2, y2 = map(float, input("Введите координаты вершины B через пробел: ").split())
x3, y3 = map(float, input("Введите координаты вершины C через пробел: ").split())

triangle_a = triangle(x1, y1, x2, y2, x3, y3)
print(f"Площадь треугольника равна {triangle_a}")
#2
arr = []
for i in range(15):
    num = int(input("Введите элемент массива: "))
    arr.append(num)
zero_indices = [i for i, x in enumerate(arr) if x == 0]
print("Номера нулевых элементов в массиве:", zero_indices)
last_positive_index = -1
for i in range(len(arr)):
    if arr[i] > 0:
        last_positive_index = i
print("Номер последнего положительного элемента:", last_positive_index)
#3
arr = []
for i in range(17):
    num = int(input("Введите элемент массива: "))
    arr.append(num)
s = 0
for num in arr:
    if num < 0:
        break
    s += num
print("Сумма всех элементов до первого отрицательного равна:", s)
#4
a = []
b = []
print("Введите элементы первого массива:")
for i in range(10):
    num = int(input("Введите элемент: "))
    a.append(num)
print("Введите элементы второго массива:")
for i in range(10):
    num = int(input("Введите элемент: "))
    b.append(num)
if a  == b:
    print("Массивы равны")
else:
    print("Массивы не равны")
if a != b:
    print("Массивы неравны")
else:
    print("Массивы равны")
#5
a = []
for i in range(20):
    num = int(input("Введите элемент массива: "))
    a.append(num)
s = [i for i, x in enumerate(a) if x == 0]
print("Массив из номеров нулевых элементов:", s)