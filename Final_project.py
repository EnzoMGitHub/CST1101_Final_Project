import tkinter as tk
from tkinter import filedialog
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS

class Word_frequency_analyzer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Final Project")
        self.file_path = tk.StringVar()
        self.analysis_type = tk.StringVar()
        self.stopwords_var = tk.BooleanVar()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select a Text File:").pack(pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_file).pack(pady=5)
        tk.Label(self.root, text="Select Analysis Type:").pack(pady=10)
        tk.Radiobutton(self.root, text="Word Frequencies", variable=self.analysis_type, value="word").pack()
        tk.Radiobutton(self.root, text="Character Frequencies", variable=self.analysis_type, value="char").pack()
        tk.Checkbutton(self.root, text="Filter Stopwords", variable=self.stopwords_var).pack(pady=10)
        tk.Button(self.root, text="Analyze", command=self.analyze).pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        self.file_path.set(file_path)

    def analyze(self):
        file_path = self.file_path.get()
        analysis_type = self.analysis_type.get()
        filter_stopwords = self.stopwords_var.get()

        if not file_path:
            self.show_error("Please select a text file.")
            return
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            if analysis_type == "word":
                frequencies = self.get_word_frequencies(content, filter_stopwords)
                title = "Word Frequencies"
            elif analysis_type == "char":
                frequencies = self.get_char_frequencies(content)
                title = "Character Frequencies"
            else:
                self.show_error("Invalid analysis type.")
                return
            self.plot_bar_chart(frequencies, title)
        except Exception as e:
            self.show_error(f"An error occurred: {str(e)}")
    def get_word_frequencies(self, content, filter_stopwords):
        words = content.lower().split()
        if filter_stopwords:
            words = [word for word in words if word not in STOPWORDS]
        return Counter(words)
    
    def get_char_frequencies(self, content):
        return Counter(content.lower())
    
    def plot_bar_chart(self, frequencies, title):
        plt.bar(frequencies.keys(), frequencies.values())
        plt.title(title)
        plt.xlabel("Words" if title == "Word Frequencies" else "Characters")
        plt.ylabel("Frequency")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        file_path = self.file_path.get()
        save_path = file_path.rsplit('.', 1)[0] + "_" + title.lower().replace(" ", "_") + ".png"
        plt.savefig(save_path)
        plt.show()

    def show_error(self, message):
        tk.messagebox.showerror("Error", message)
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    analyzer = Word_frequency_analyzer()
    analyzer.run()
