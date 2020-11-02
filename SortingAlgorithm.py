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
    

def quick_sort(data : list, draw_sort, sec : int, head : int, tail : int):

    if head < tail:
        i_partition = partition(data, draw_sort, sec, head, tail)

        # Left partition
        quick_sort(data, draw_sort, sec, head, i_partition - 1)

        # Right partition
        quick_sort(data, draw_sort, sec, i_partition + 1, tail)


def partition(data : list, draw_sort, sec : int, head : int, tail : int):
    '''
    Args:

    Return:

    '''
    border = head
    pivot = data[tail]

    draw_sort(data, get_color_array(len(data), head, tail, border, border))
    time.sleep(sec)

    for i in range(head, tail):
        if data[i] < pivot:
            draw_sort(data, get_color_array(len(data), head, tail, border, i, True))
            time.sleep(sec)
            data[border], data[i] = data[i], data[border]
            border += 1

        draw_sort(data, get_color_array(len(data), head, tail, border, i))
        time.sleep(sec)

    # Swap pivot with border value
    draw_sort(data, get_color_array(len(data), head, tail, border, tail, True))
    time.sleep(sec)
    data[border], data[tail] = data[tail], data[border]

    return border


def get_color_array(data_len : int, head : int, tail : int, border : int, curr_i : int, is_swaping : bool = False):
    color_array = []

    for i in range(data_len):
        if i >= head and i <= tail:
            color_array.append('gray')
        else:
            color_array.append('white')
        
        if i == tail:
            color_array[i] = 'blue'
        elif i == border:
            color_array[i] = 'red'
        elif i == curr_i:
            color_array[i] = 'yellow'
        
        if is_swaping:
            if i == border or i == curr_i:
                color_array[i] = 'green'

    return color_array
