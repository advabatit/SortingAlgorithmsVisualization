import time

def bubble_sort(data : list, draw_sort, sec : int):
    """
    Fucntion that using the bubble sort algorithm to sort a list
    Args:
        data (list): To sort
        draw_sort (function): Function that we use to draw the difference in every increasment of k 
        sec (int): How much time to delay
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
    """
    Fucntion that using the quick sort algorithm to sort a list
    Args:
        data (list): To sort
        draw_sort (function): Function that we use to draw the difference in every increasment of k 
        sec (int): How much time to delay
        head (int): The index of the head of the list
        tail (int): The index of the tail of the list
    Return:
        Nothing
    """
    if head < tail:
        i_partition = partition(data, draw_sort, sec, head, tail)

        # Left partition
        quick_sort(data, draw_sort, sec, head, i_partition - 1)

        # Right partition
        quick_sort(data, draw_sort, sec, i_partition + 1, tail)


def partition(data : list, draw_sort, sec : int, head : int, tail : int) -> int:
    '''
    Function that patrition the list in order to sort it
    Args:
        data (list): To sort
        draw_sort (function): Function that we use to draw the difference in every increasment of k 
        sec (int): How much time to delay
        head (int): The index of the head of the list
        tail (int): The index of the tail of the list
    Return:
        border (int): It returns the border index
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
    '''
    Function that create the color list of the quick sort algorithm
    Args:
        data_len (int): The length of data
        head (int): The index of the head of the list
        tail (int): The index of the tail of the list
        border (int): The index of the border
        curr_i (int): The current index we are on
        is_swaping (bool): Boolean variable that allows the function to know if swap happend
    Return:
        color_list (list): It returns the color list
    '''

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
    """
    Function that starts the merge sort algorithm
    Args:
        data (list): The data we need to sort
        sec (int): The time we delay the sorting algorithm
    Return:
        Nothing
    """

    merge_sort_algorithm(data, 0, len(data) - 1, draw_sort, sec)

def merge_sort_algorithm(data : list, left : int, right : int, draw_sort, sec : int):
    """
    Function that use the merge algorithm to sort a list
    Args:
        data (list): The data we need to sort
        left (int): The left side index
        right (int): The right side index
        draw_sort (function): Function that we use to draw the difference in every time we move element
        sec (int): The time we delay the sorting algorithm
    Return:
        Nothing
    """

    if left < right:
        mid = (left + right) // 2
        merge_sort_algorithm(data, left, mid, draw_sort, sec)
        merge_sort_algorithm(data, mid + 1, right, draw_sort, sec)
        merge(data, left, mid, right, draw_sort, sec)

def merge(data : list, left : int, mid : int, right : int, draw_sort, sec: int):
    """
    Function that merge the left and right side to one sorted list
    Args:
        data (list): The data we need to sort
        left (int): The left side index
        mid (int): The mid index
        right (int): The right side index
        draw_sort (function): Function that we use to draw the difference in every time we move element
        sec (int): The time we delay the sorting algorithm
    Return:
        Nothing
    """

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

def get_color_list_merge_sort(length : int, right : int, left : int, mid : int) -> list:
    '''
    Function that create the color list of the merge sort algorithm
    Args:
        length (int) : The length of the list we sort
        right (int): The index of the right element of the list
        left (int): The index of the left element of the list
        mid (int): The index of the mid element of the list
    Return:
        color_list (list): It returns the color list
    '''

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