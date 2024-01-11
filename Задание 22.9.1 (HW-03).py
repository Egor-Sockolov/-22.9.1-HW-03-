while True:
    try:
        sequence_num = list(map(int, input("Введите последовательность чисел: ").split()))
        if len(sequence_num) <= 3:
            print("Введите минимум четыре числа")
        else:
            break
    except ValueError:
        print("Некорректный ввод")
print(sequence_num)

while True:
    try:
        random_num = int(input("Выберите одно из введеных чисел: "))
        if random_num <= 0:
            print("Число должно быть больше 0")
        else:
            break
    except ValueError:
        print("Некорректный ввод")

def merge_sort(sequence_num):
    if len(sequence_num) < 2:
        return sequence_num[:]
    else:
        middle = len(sequence_num) // 2
        left = merge_sort(sequence_num[:middle])
        right = merge_sort(sequence_num[middle:])
        return merge(left, right)

def merge(left, right):
    results = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1
    while i < len(left):
        results.append(left[i])
        i += 1
    while j < len(right):
        results.append(right[j])
        j += 1
    return results

sequence_num = merge_sort(sequence_num)
print(sequence_num)

def binary_search(sequence_num, random_num, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if sequence_num[middle] == random_num:
        return middle
    elif random_num < sequence_num[middle]:
        return binary_search(sequence_num, random_num, left, middle - 1)
    else:
        return binary_search(sequence_num, random_num, middle + 1, right)


position = binary_search(sequence_num, random_num, 0, len(sequence_num) - 1)

if random_num == sequence_num[0]:
    print(f"Число {random_num} самое маленькое!")
elif random_num == max(sequence_num):
    print(f"Число {random_num} самое большое!")
elif sequence_num[position] == random_num:
    print(f"Число {random_num} больше чем число на {position}-ой позиции, но меньше или равно числу на {position+2} позиции")
else:
    print(f"Число {random_num} отсутствует!")


