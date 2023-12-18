from tkinter import ttk, filedialog
import tkinter as tk  
import matplotlib.pyplot as plot
from collections import Counter

initial_words = ''
dictionary = {}
char_dict = {}
msg_count = 0

def remove_punctuation(string):
    return ''.join(char for char in string if char.isalnum() or char.isspace())

def word_frequencies(text):
    words = text.split()
    return Counter(words)

def char_frequencies(text):
    cleaned_text = remove_punctuation(text)
    return Counter(cleaned_text)

def plot_words():
    plot.bar(dictionary.keys(), dictionary.values())
    plot.show()

def plot_chars():
    plot.bar(char_dict.keys(), char_dict.values())
    plot.show()

def create_var():
    global initial_words, dictionary, char_dict, msg_count
    try:
        file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
        with open(file_path, 'r') as file:
            initial_words = file.read()
        dictionary = word_frequencies(initial_words)
        char_dict = char_frequencies(initial_words)
    except FileNotFoundError:
        handle_error('Please select a text file after clicking the open file button')
    except UnicodeDecodeError:
        handle_error('Please select a valid text file')

def handle_error(error_message):
    global msg_count
    for widget in frm.grid_slaves(column=0, row=5):
        widget.destroy()
    message_err = ttk.Label(frm, text=error_message)
    message_err.grid(column=0, row=5)
    ttk.Label(frm, text=f'{msg_count + 1}. {error_message}').grid(column=0, row=msg_count + 6)
    msg_count += 1

def gen():
    global msg_count
    try:
        if value.get() == 0:
            handle_error('Please Select Either Word Mode Or Character Mode')
        elif value.get() == 1:
            plot_words()
        elif value.get() == 2:
            plot_chars()
    except NameError:
        handle_error('Please Select A Text File Before Generating')

def down():
    global msg_count
    try:
        if value.get() == 0:
            handle_error('Please Select Either Word Mode Or Character Mode')
        elif value.get() == 1 or value.get() == 2:
            plot.bar(dictionary.keys(), dictionary.values())
            plot.savefig('graph.png')
            for widget in frm.grid_slaves(column=0, row=5):
                widget.destroy()
            message_down = ttk.Label(frm, text='Successfully saved as \'graph.png\'!')
            message_down.grid(column=0, row=5)
            ttk.Label(frm, text=f'{msg_count + 1}. Successfully saved as \'graph.png\'!').grid(column=0, row=msg_count + 6)
            msg_count += 1
    except NameError:
        handle_error('Please Select A Text File Before Downloading')

root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
frame_mode = ttk.LabelFrame(frm, text='Select Analysis Mode')
frame_mode.grid(column=0, row=0, padx=10, pady=10, sticky='W')
frame_buttons = ttk.Frame(frm)
frame_buttons.grid(column=0, row=1, pady=10)
value = tk.IntVar()

ttk.Radiobutton(frame_mode, text='Word Mode', command=plot_words, value=1, variable=value).grid(column=0, row=0, sticky='W')
ttk.Radiobutton(frame_mode, text='Character Mode', command=plot_chars, value=2, variable=value).grid(column=1, row=0, sticky='W')
ttk.Button(frame_buttons, text='Open File', command=create_var).grid(column=0, row=0, padx=5)
ttk.Button(frame_buttons, text='Generate', command=gen).grid(column=1, row=0, padx=5)
ttk.Button(frame_buttons, text='Download', command=down).grid(column=2, row=0, padx=5)

root.mainloop()

