import tkinter
from tkinter import ttk

MAX_WIDTH, MAX_HEIGHT = 900, 600
FRAME_WIDTH, FRAME_HEIGHT = 600, 200
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 380
PAD_X_LAYOUT, PAD_Y_LAYOUT = 10, 5
PAD_X, PAD_Y = 5, 5


def main():
    root = tkinter.Tk()
    root.title("Sorting Algorithms Visualization")
    root.maxsize(MAX_WIDTH, MAX_HEIGHT)
    root.config(bg='black')

    # Base layoutt
    UI_frame = tkinter.Frame(root, width = FRAME_WIDTH, height = FRAME_HEIGHT, bg = 'grey')
    UI_frame.grid(row = 0, column = 0, padx = PAD_X_LAYOUT, pady = PAD_Y_LAYOUT)

    canvas = tkinter.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = 'white')
    canvas.grid(row = 1, column = 0, padx = PAD_X_LAYOUT, pady = PAD_Y_LAYOUT)
    
    # Variables 
    selected_algorithm = tkinter.StringVar()
    algorithm_list = ['Bubble Sort', 'Merge Sort']

    # TO DO: Create function to crate labels more generic
    # TO DO: Create function to create entry more generic

    algorithm_label = tkinter.Label(UI_frame, text = 'Algorithm', bg = 'grey')
    algorithm_label.grid(row = 0, column = 0, padx = PAD_X, pady = PAD_Y, sticky = 'W')

    algorithm_menu = ttk.Combobox(UI_frame, textvariable = selected_algorithm, values = algorithm_list)
    algorithm_menu.grid(row = 0, column = 1, padx = PAD_X, pady = PAD_Y, sticky = 'W')
    algorithm_menu.current(0)

    generate_button = tkinter.Button(UI_frame, text = 'Generate', command = lambda : generat(selected_algorithm, canvas))
    generate_button.grid(row = 0, column = 2, padx = PAD_X, pady = PAD_Y, sticky = 'W')

    size_label = tkinter.Label(UI_frame, text = 'Size', bg = 'grey')
    size_label.grid(row = 1, column = 0, padx = PAD_X, pady = PAD_Y, sticky = 'W')
    size_entery = tkinter.Entry(UI_frame)
    size_entery.grid(row = 1, column = 1, padx = PAD_X, pady = PAD_Y, sticky = 'W')

    min_value_label = tkinter.Label(UI_frame, text = 'Min Value', bg = 'grey')
    min_value_label.grid(row = 1, column = 2, padx = PAD_X, pady = PAD_Y, sticky = 'W')
    min_value_entery = tkinter.Entry(UI_frame)
    min_value_entery.grid(row = 1, column = 3, padx = PAD_X, pady = PAD_Y, sticky = 'W')

    max_value_label = tkinter.Label(UI_frame, text = 'Max Value', bg = 'grey')
    max_value_label.grid(row = 1, column = 4, padx = PAD_X, pady = PAD_Y, sticky = 'W')
    max_value_entery = tkinter.Entry(UI_frame)
    max_value_entery.grid(row = 1, column = 5, padx = PAD_X, pady = PAD_Y, sticky = 'W')


    root.mainloop()


def generat(selected_algorithm : tkinter.StringVar, canvas : tkinter.Canvas):
    print(selected_algorithm.get())
    data = [100, 200, 200, 300]
    draw_sort(data, canvas)


def draw_sort(data : list, canvas : tkinter.Canvas):
    x_width = CANVAS_WIDTH / (len(data) + 1)
    offset = 30
    space = 10
    for i, height in enumerate(data):
        # Top left
        x_start = i * x_width + offset + space
        y_start = CANVAS_HEIGHT - height
        
        # Bottom right
        x_end = (i + 1) * x_width + offset
        y_end = CANVAS_HEIGHT

        canvas.create_rectangle(x_start, y_start, x_end, y_end, fill='red')
        canvas.create_text(x_start + 2, y_start, anchor='sw', text = str(data[i]))


if __name__ == '__main__':
    main()