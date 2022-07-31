#Задайте список из n чисел последовательности 
#$(1+\frac 1 n)^n$ и выведите на экран их сумму.

#Пример:
#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Введите число N: "))
result_array = [0] * n
summ = 0
for i in range(n):
    result_array[i] = (1 + 1/(i + 1))**(i+1)
    summ += result_array[i]

print(f"Последовательность: \r\n {result_array}")
print(f"Сумма: {summ}")