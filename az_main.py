import tkinter as tk
from tkinter import filedialog
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def analyze_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()  
        words = text.split() 
        word_counts = Counter(words)  
        most_common_words = word_counts.most_common(10)  
        return most_common_words

def plot_bar_graph(words_and_counts):
    plt.clf()  
    words, counts = zip(*words_and_counts)
    plt.bar(words, counts, color='blue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 10 Most Common Words')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        most_common_words = analyze_text(file_path)
        plot_bar_graph(most_common_words)
        canvas.draw()

root = tk.Tk()
root.title('Word Frequency Analyzer')

frame = tk.Frame(root)
frame.pack()

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

root.mainloop()
