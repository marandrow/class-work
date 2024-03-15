#1

todo_list = [ 'cook breakfest', 'go to shop', ' do homework']

for item in todo_list:
    print(item)

todo_list.append('walk with dog')
print(todo_list)
for item in todo_list:
    print(item)

#2

shopping_list = ['apple', ' milk ', ' bread ', ' meat ', ' eggs ']

for item1 in shopping_list:
    if item1 == ' milk ' or item1 == ' eggs ':
        print( f' buy {item1} 2 times. ')
    else:
        print( f' buy {item1} 1 time. ')

#3

a = int(input(' Введите число \n >'))
b = 0

if a <= 30:
    for i in range (0, a):
        b += 1
        print(b)
else:
    pass

#4

password = input ()

for
#WHILE

# 1

string = input('Введите строку \n > ')

print('Используется цикл while: ')
i = 0
while i < len(string):
    print(f'{string[i]} : {ord(string[i])}')
    i += 1
print('\nИспользование цикла for:')
for char in string:
    print(f'{char} : {ord(char)}')

# 2

n = int(input('Enter a positive integer: '))
while n <= 0:
    print('Invalid input. Please enter a positive integer.')
    n = int(input('Enter a positive integer: '))
sum_of_squares = 0
for i in range(1, n + 1):
    sum_of_squares += i ** 2
print(f' The sum of the square of the first {n} nature numbers is: {sum_of_squares}')

# 3

c = int(input('Введите число кратное 3\n > '))
b = 0

while c % 3 != 0:
    c = int(input('Введеённое число не кратно трём \n Введите число кратное 3 \n > '))
for i in range(0, c):
    a = c * b
    b += 1
    print(a)
