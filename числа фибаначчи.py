a = int(input("Введите количество чисел ряда Фибаначи:"))
v = 0
c = 1
print(v)
print(c)
i = 2
while i < a:
    s = v + c 
    print(s)
    v = c 
    c = s 
    i = i + 1
