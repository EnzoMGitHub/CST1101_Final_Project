
# Word Frequency Calculator 
import tkinter
from tkinter import ttk, filedialog
import matplotlib.pyplot as plot

msg_count = 0

def remove_punctuation(string):
    ret = ''
    for i in string:
        if i.lower() in 'abcdefghijklmnopqrstuvwxyz':
            ret = ret + i.lower()
    return ret
def frequency(lis, word):
    count = 0
    for i in lis:
        if i == word:
            count = count + 1
    return count/len(lis)
def remove_duplicates(lis):
    ret = list()
    for i in lis:
        if i.lower() in ret:
            continue
        else:
            ret.append(i.lower())
    return ret
def merge(lis1,lis2):
    return {lis1[n]:lis2[n] for n in range(len(lis1))}
def word_frequencies(initial_words):
    init_change = initial_words.split()
    words = list()
    no_dupe = list()
    for i in init_change:
        words.append(remove_punctuation(i))

    no_dupe = remove_duplicates(words)

    counts = list()
    for i in no_dupe:
        counts.append(frequency(words,i))
    
    return merge(no_dupe,counts)

def char_frequencies(lis):
    chars = list(''.join(initial_words).lower())
    no_dupe_chars = remove_duplicates(chars)
    freqs = list()
    for i in no_dupe_chars:
        freqs.append(frequency(chars,i))
        
    return merge(no_dupe_chars,freqs)

    
def plot_words():
    plot.bar(dictionary.keys(),dictionary.values())
    # plot.xticks(rotation=70)
    plot.show()
def convertdirectory(dir):
    new_dir = dir.split('/')
    new_dir.remove(new_dir[-1])
    new_str = '/'.join(new_dir)
    return new_str

def plot_chars():
    global chars
    plot.bar(char_dict.keys(),char_dict.values())
    plot.savefig('graph.png')
    plot.show()

def create_var():
    global initial_words,dictionary,char_dict,msg_count
    try:
        file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
        with open(file_path, 'r') as file:
            initial_words = file.read()
        dictionary = word_frequencies(initial_words)
        char_dict = char_frequencies(initial_words)
    except FileNotFoundError:
        ttk.Label(frm,text=str(msg_count + 1) + '. Please select a text file after clicking the open file button').grid(column=0,row=msg_count+6)
        msg_count = msg_count + 1
    except UnicodeDecodeError: # Error gets raised if you try to convert a given file type and open it in the program, which raises the UnicodeDecodeError
        ttk.Label(frm,text=str(msg_count + 1) + '. Please select a text file').grid(column=0,row=msg_count+6)
        msg_count = msg_count + 1
    
def gen():
    global msg_count
    try:
        if value.get() == 0:
            ttk.Label(frm,text=str(msg_count + 1) + '. Please Select Either Word Mode Or Character Mode').grid(column=0,row=msg_count+6)
            msg_count = msg_count + 1
        elif value.get() == 1:
            plot_words()
        elif value.get() == 2:
            plot_chars()
    except NameError:
        ttk.Label(frm,text=str(msg_count + 1) + '. Please Select A Text File Before Generating').grid(column=0,row=msg_count+6)
        msg_count = msg_count + 1

def down():
    global msg_count
    if value.get() == 0:
        ttk.Label(frm,text=str(msg_count + 1) + '. Please Select Either Word Mode Or Character Mode').grid(column=0,row=msg_count+6)
        msg_count = msg_count + 1
    elif value.get() == 1:
        plot.bar(dictionary.keys(),dictionary.values())
        plot.savefig('graph.png')
        ttk.Label(frm,text=str(msg_count + 1) + '. Successfuly saved as \'graph.png\'!').grid(column=0,row=msg_count+6)
        msg_count = msg_count + 1
    elif value.get() == 2:
        plot.bar(char_dict.keys(),char_dict.values())
        plot.savefig('graph.png')
        ttk.Label(frm,text=str(msg_count + 1) + '. Successfuly saved as \'graph.png\'!').grid(column=0,row=msg_count+6)
        msg_count = msg_count + 1




root = tkinter.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
value = tkinter.IntVar()
ttk.Radiobutton(frm,text='Word Mode',value=1,variable=value).grid(column=0,row=1)
ttk.Radiobutton(frm,text='Character Mode',value=2,variable=value).grid(column=0,row=2)
ttk.Button(frm, text='Open File', command=create_var).grid(column=0,row=3)
ttk.Button(frm,text='Generate', command=gen).grid(column=0,row=4)
ttk.Button(frm,text='Download', command=down).grid(column=0,row=5)

root.mainloop()
