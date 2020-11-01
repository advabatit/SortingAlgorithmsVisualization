import tkinter
import time

def bubble_sort(data : list, draw_sort, sec):
    
    for i in range(len(data)):
        for k in range(len(data) - 1 - i):
            if data[k] > data[k + 1]:
                data[k], data[k + 1] = data[k + 1], data[k]
                draw_sort(data, ['green' if x == k or x == k + 1 else 'red' for x in range(len(data))])
                time.sleep(sec)
    draw_sort(data, ['green' for _ in range(len(data))])
            
def binary_search(num : int, data : list, end : int, start : int = 0):

    mid = (end + start) // 2
    print(mid)

    if end < start:
        print(f"The number {num} is not in the list")
        return -1

    if data[mid] == num:
        print(f"Found the number {num} in the list")
        return mid

    elif num > data[mid]:
        return binary_search(num, data, start = mid + 1, end = end)

    else:
        return binary_search(num, data, start, end = mid - 1)
