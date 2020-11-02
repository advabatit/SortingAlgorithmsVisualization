import tkinter
from tkinter import ttk
import random
from SortingAlgorithm import bubble_sort, quick_sort


MAX_WIDTH, MAX_HEIGHT = 900, 600
FRAME_WIDTH, FRAME_HEIGHT = 600, 200
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 380
PAD_X_LAYOUT, PAD_Y_LAYOUT = 10, 5
PAD_X, PAD_Y = 5, 5

root = tkinter.Tk()
UI_frame = tkinter.Frame(root, width = FRAME_WIDTH, height = FRAME_HEIGHT, bg = 'grey')
canvas = tkinter.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = 'white')
scales_data = [[0, 10, 'Select Size'],
                [0, 10, 'Select min value'],
                [11, 100, 'Select max value']]
                
data = []

def main():
    # Variables 
    selected_algorithm = tkinter.StringVar()
    algorithm_list = ['Bubble Sort', 'Quick Sort', 'Merge Sort']
    buttons_data = [['Start', lambda : start_algorithm(algorithm_menu, speed_scale.get())],
                    ['Generate', lambda : generat(min_value_entery, max_value_entery, size_entery)]]

    base_layout()

    algorithm_label = tkinter.Label(UI_frame, text = 'Algorithm', bg = 'grey')
    algorithm_label.grid(row = 0, column = 0, padx = PAD_X, pady = PAD_Y, sticky = 'W')

    algorithm_menu = ttk.Combobox(UI_frame, textvariable = selected_algorithm, values = algorithm_list)
    algorithm_menu.grid(row = 0, column = 1, padx = PAD_X, pady = PAD_Y, sticky = 'W')
    algorithm_menu.current(0)

    size_entery, min_value_entery, max_value_entery, speed_scale = init_scale()
    init_buttons(buttons_data)

    root.mainloop()


def base_layout():
    """
    Function that initialize the base layout
    Args:
        Nothing
    Return:
        Nothing
    """

    root.title("Sorting Algorithms Visualization")
    root.maxsize(MAX_WIDTH, MAX_HEIGHT)
    root.config(bg='black')    
    
    UI_frame.grid(row = 0, column = 0, padx = PAD_X_LAYOUT, pady = PAD_Y_LAYOUT)
    canvas.grid(row = 1, column = 0, padx = PAD_X_LAYOUT, pady = PAD_Y_LAYOUT)

def init_scale():
    """
    Function that initalize the scales (size, min value, max value and speed)
    Args:
        Nothing
    Return:
        Min value (int), Max value (int), size (int) and speed (int)
    """

    global scales_data
    values = [] # values[0] = size, values[1] = min, values[2] = max

    for i in range(len(scales_data)):
        values.append(tkinter.Scale(UI_frame, from_ = scales_data[i][0], to = scales_data[i][1], resolution = 1, orient = 'horizontal', label = scales_data[i][2]))
        values[i].grid(row = 1, column = i, padx = PAD_X, pady = PAD_Y)

    speed_scale = tkinter.Scale(UI_frame, from_ = 0.1, to = 2.0, length = 200, digits = 2, resolution = 0.2, orient = 'horizontal', label = 'Select speed [s]')
    speed_scale.grid(row = 0, column = 2, padx = PAD_X, pady = PAD_Y)

    return values[0], values[1], values[2], speed_scale

def init_buttons(buttons_data : list):
    """
    Function that initalize the buttons
    Args:
        The buttons data (list): it contains the label of the button and the function (with args if exists)
    Return:
        Nothing
    """
    
    values = []

    for i in range(len(buttons_data)):
        values.append(tkinter.Button(UI_frame, text = buttons_data[i][0], command = buttons_data[i][1]))
        values[i].grid(row = i, column = 3, padx = PAD_X, pady = PAD_Y, sticky = 'W')

def generat(min : tkinter.Entry, max : tkinter.Entry, size_entery : tkinter.Entry):
    """
    Function that generate the data and present it to the screen
    Args:
        min entry (tkinter.Entry): represent the min value the user enter   
        max entry (tkinter.Entry): represent the max value the user enter
        size entry (tkinter.Entry): represent the size the user enter
    Return:
        Nothing
    """

    global data
    data = []

    data = get_data(min, max, size_entery)
    draw_sort(data, ['red' for x in range(len(data))])

def get_data(min : tkinter.Entry, max : tkinter.Entry, size_entery : tkinter.Entry) -> list:
    """
    Function gets the values from the tkinter.Entry and set the data list
    Args:
        min entry (tkinter.Entry): represent the min value the user enter
        max entry (tkinter.Entry): represent the max value the user enter
        size entry (tkinter.Entry): represent the size the user enter
    Return:
        data (list): the list we will need to sort later
    """

    global data

    min_val = int(min.get())
    max_val = int(max.get())
    size = int(size_entery.get())

    for _ in range (size):
        data.append(random.randrange(min_val, max_val + 1))
    
    return data

def draw_sort(data : list, color : list):
    """
    Function that draw the data to the screen
    Args:
        data (list): the data we need to sort
        color (list): which number to fill with which color (green or red)
    Return:
        Nothing
    """

    canvas.delete('all')

    x_width = CANVAS_WIDTH / (len(data) + 1)
    offset = 30
    space = 10
    normalize_data = [i / max(data) for i in data]

    for i, height in enumerate(normalize_data):
        # Top left
        x_start = i * x_width + offset + space
        y_start = CANVAS_HEIGHT - height * (CANVAS_HEIGHT - 40)
        
        # Bottom right
        x_end = (i + 1) * x_width + offset
        y_end = CANVAS_HEIGHT

        canvas.create_rectangle(x_start, y_start, x_end, y_end, fill = color[i])
        canvas.create_text(x_start + 2, y_start, anchor='sw', text = str(data[i]))

    root.update_idletasks()

def start_algorithm(algorithm_menu : ttk.Combobox, sec : int):
    global data
    if not data: print("There is no data to sort")

    if algorithm_menu.get() == 'Bubble Sort':
        bubble_sort(data, draw_sort, sec)

    elif algorithm_menu.get() == 'Quick Sort':
        quick_sort(data, draw_sort, sec, 0, len(data) - 1)
        draw_sort(data, ['green' for _ in range(len(data))])

if __name__ == '__main__':
    main()