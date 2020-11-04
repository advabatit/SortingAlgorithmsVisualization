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


def partition(data : list, draw_sort, sec : int, head : int, tail : int) -> int:
    '''
    Args:

    Return:

    '''
    border = head
    pivot = data[tail]

    draw_sort(data, get_color_list_quick_sort(len(data), head, tail, border, border))
    time.sleep(sec)

    for i in range(head, tail):
        if data[i] < pivot:
            draw_sort(data, get_color_list_quick_sort(len(data), head, tail, border, i, True))
            time.sleep(sec)
            data[border], data[i] = data[i], data[border]
            border += 1

        draw_sort(data, get_color_list_quick_sort(len(data), head, tail, border, i))
        time.sleep(sec)

    # Swap pivot with border value
    draw_sort(data, get_color_list_quick_sort(len(data), head, tail, border, tail, True))
    time.sleep(sec)
    data[border], data[tail] = data[tail], data[border]

    return border


def get_color_list_quick_sort(data_len : int, head : int, tail : int, border : int, curr_i : int, is_swaping : bool = False) -> list:
    color_list = []

    for i in range(data_len):
        if i >= head and i <= tail:
            color_list.append('gray')
        else:
            color_list.append('white')
        
        if i == tail:
            color_list[i] = 'blue'
        elif i == border:
            color_list[i] = 'red'
        elif i == curr_i:
            color_list[i] = 'yellow'
        
        if is_swaping:
            if i == border or i == curr_i:
                color_list[i] = 'green'

    return color_list


def merge_sort(data : list, draw_sort, sec : int):
    merge_sort_algorithm(data, 0, len(data) - 1, draw_sort, sec)

def merge_sort_algorithm(data : list, left : int, right : int, draw_sort, sec : int):
    
    if left < right:
        mid = (left + right) // 2
        merge_sort_algorithm(data, left, mid, draw_sort, sec)
        merge_sort_algorithm(data, mid + 1, right, draw_sort, sec)
        merge(data, left, mid, right, draw_sort, sec)

def merge(data : list, left : int, mid : int, right : int, draw_sort, sec: int):
    
    draw_sort(data, get_color_list_merge_sort(len(data), right, left, mid))
    time.sleep(sec)

    left_part = data[left : mid + 1]
    rigth_part = data[mid + 1 : right + 1]

    i_right = i_left = 0

    for data_index in range(left, right + 1):
        if i_left < len(left_part) and i_right < len(rigth_part):
            if left_part[i_left] <= rigth_part[i_right]:
                data[data_index] = left_part[i_left]
                i_left += 1
            else:
                data[data_index] = rigth_part[i_right]  
                i_right += 1
        
        elif i_left < len(left_part):
            data[data_index] = left_part[i_left]
            i_left += 1
        else:
            data[data_index] = rigth_part[i_right]  
            i_right += 1

    draw_sort(data, ['green' if x >= left and x <= right else 'white' for x in range(len(data))])
    time.sleep(sec)

def get_color_list_merge_sort(length, right, left, mid) -> list:
    color_list = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i<=mid:
                color_list.append('yellow')
            else:
                color_list.append('pink')
        else:
            color_list.append('white')



    return color_list