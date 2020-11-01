import time

def bubble_sort(data : list, draw_sort, sec : int):
    """
    Fucntion that using the bubble sort algorithm to sort a list
    Args:
        data (list): to sort
        draw_sort (function): function that we use to draw the difference in every increasment of k 
        sec (int) how much time to delay
    Return:
        Nothing
    """

    for i in range(len(data)):
        for k in range(len(data) - 1 - i):
            if data[k] > data[k + 1]:
                data[k], data[k + 1] = data[k + 1], data[k]
                draw_sort(data, ['green' if x == k or x == k + 1 else 'red' for x in range(len(data))])
                time.sleep(sec)
    draw_sort(data, ['green' for _ in range(len(data))])
            