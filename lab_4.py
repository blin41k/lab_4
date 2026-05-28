import random
import time
import threading


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def parallel_quicksort(arr, k):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    left_result = []
    right_result = []

    def sort_left():
        nonlocal left_result
        left_result = parallel_quicksort(left, k - 1)

    if k > 0:
        t = threading.Thread(target=sort_left)
        t.start()

        right_result = parallel_quicksort(right, k - 1)

        t.join()
    else:
        left_result = parallel_quicksort(left, 0)
        right_result = parallel_quicksort(right, 0)

    return left_result + middle + right_result


def measure_time(func, arr, *args):
    start = time.time()
    func(arr, *args) if args else func(arr)
    end = time.time()
    return end - start


sizes = [1000, 5000, 10000, 20000, 50000]
normal_times = []
times_2 = []
times_4 = []
times_8 = []

print("N | Обычная | 2 потока | 4 потока | 8 потоков")

for size in sizes:
    arr = [random.randint(0, 100000) for _ in range(size)]

    t_normal = measure_time(quicksort, arr)
    t_2 = measure_time(parallel_quicksort, arr, 1)
    t_4 = measure_time(parallel_quicksort, arr, 2)
    t_8 = measure_time(parallel_quicksort, arr, 3)

    normal_times.append(t_normal)
    times_2.append(t_2)
    times_4.append(t_4)
    times_8.append(t_8)

    print(size, "|", t_normal, "|", t_2, "|", t_4, "|", t_8)

print("\nТаблица ускорения")
print("N | Speedup 2 | Speedup 4 | Speedup 8")

for i in range(len(sizes)):
    speedup_2 = normal_times[i] / times_2[i]
    speedup_4 = normal_times[i] / times_4[i]
    speedup_8 = normal_times[i] / times_8[i]

    print(sizes[i], "|", speedup_2, "|", speedup_4, "|", speedup_8)

import matplotlib.pyplot as plt

plt.plot(sizes, normal_times, marker='o', label='Обычная быстрая сортировка')
plt.plot(sizes, times_2, marker='o', label='2 потока')
plt.plot(sizes, times_4, marker='o', label='4 потока')
plt.plot(sizes, times_8, marker='o', label='8 потоков')

plt.xlabel('Количество элементов в массиве')
plt.ylabel('Время выполнения, с')
plt.title('Сравнение последовательной и параллельной быстрой сортировки')
plt.legend()
plt.grid(True)
plt.show()