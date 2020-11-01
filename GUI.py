import tkinter
from tkinter import ttk
import random
from SortingAlgorithm import bubble_sort


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
    algorithm_list = ['Bubble Sort', 'Merge Sort']
    buttons_data = [['Start', lambda : start_sort(speed_scale.get())],
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
    root.title("Sorting Algorithms Visualization")
    root.maxsize(MAX_WIDTH, MAX_HEIGHT)
    root.config(bg='black')    
    
    UI_frame.grid(row = 0, column = 0, padx = PAD_X_LAYOUT, pady = PAD_Y_LAYOUT)
    canvas.grid(row = 1, column = 0, padx = PAD_X_LAYOUT, pady = PAD_Y_LAYOUT)

def init_scale():
    global scales_data
    values = [] # values[0] = size, values[1] = min, values[2] = max

    for i in range(len(scales_data)):
        values.append(tkinter.Scale(UI_frame, from_ = scales_data[i][0], to = scales_data[i][1], resolution = 1, orient = 'horizontal', label = scales_data[i][2]))
        values[i].grid(row = 1, column = i, padx = PAD_X, pady = PAD_Y)

    speed_scale = tkinter.Scale(UI_frame, from_ = 0.1, to = 2.0, length = 200, digits = 2, resolution = 0.2, orient = 'horizontal', label = 'Select speed [s]')
    speed_scale.grid(row = 0, column = 2, padx = PAD_X, pady = PAD_Y)

    return values[0], values[1], values[2], speed_scale

def init_buttons(buttons_data : list):
    values = []

    for i in range(len(buttons_data)):
        values.append(tkinter.Button(UI_frame, text = buttons_data[i][0], command = buttons_data[i][1]))
        values[i].grid(row = i, column = 3, padx = PAD_X, pady = PAD_Y, sticky = 'W')

def generat(min : tkinter.Entry, max : tkinter.Entry, size_entery : tkinter.Entry):
    global data
    data = []
    data = get_data(min, max, size_entery)
    
    draw_sort(data, ['red' for x in range(len(data))])

def start_sort(time):
    global data
    bubble_sort(data, draw_sort, time)


def get_data(min : tkinter.Entry, max : tkinter.Entry, size_entery : tkinter.Entry) -> list:
    global data

    min_val = int(min.get())
    max_val = int(max.get())
    size = int(size_entery.get())

    for _ in range (size):
        data.append(random.randrange(min_val, max_val + 1))
    
    return data

def draw_sort(data : list, color : list):
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

if __name__ == '__main__':
    main()