import time

def bubble_sort(data : list, draw_sort, sec):
    
    for i in range(len(data)):
        for k in range(len(data) - 1 - i):
            if data[k] > data[k + 1]:
                data[k], data[k + 1] = data[k + 1], data[k]
                draw_sort(data, ['green' if x == k or x == k + 1 else 'red' for x in range(len(data))])
                time.sleep(sec)
    draw_sort(data, ['green' for _ in range(len(data))])
            