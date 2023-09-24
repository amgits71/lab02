#алгоритм решето Эратосфена
#алгоритм нахождения простых чисел до заданного натурального числа путем постепенного отсеивания составных чисел

n = int(input("Введите число n: "))
numbers = [i for i in range(2, n + 1)]
primos = []

while (len(numbers) > 0):
    next_prime = numbers[0]
    primos.append(next_prime)
    numbers = numbers[1:]

    for j in range (2, len(numbers)):
        for k in range(len(numbers)):
            if next_prime * j == numbers[k]:
                numbers = numbers[:k] + numbers[k + 1:]
                break

print("Решение: ")
print(primos)