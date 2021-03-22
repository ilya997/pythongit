
old_list = []
new_list = []
i2 = 0
n = int(input('Введите кол-во чисел: '))
for _ in range(n):
    number = int(input('Введите число: '))
    old_list.append(number)
    new_list.append(0)


k = int(input('Введите сдвиг: '))
if k > n:
     while k > n:
         k -= n
for i2 in range(n):
    if i2 + k >= n:
       new_list[i2] = old_list[(i2 + k)- n]
    else:
        new_list[i2] = old_list[i2 + k]

print(new_list)




