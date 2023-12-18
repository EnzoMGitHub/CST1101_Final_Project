
# Word Frequency Calculator 
import tkinter
from tkinter import ttk, filedialog
import matplotlib.pyplot as plot


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
    
    words = list()
    no_dupe = list()
    for i in initial_words:
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
    global initial_words,dictionary,char_dict
    try:
        file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
        with open(file_path, 'r') as file:
            initial_words = file.read()
        dictionary = word_frequencies(initial_words)
        char_dict = char_frequencies(initial_words)
    except FileNotFoundError:
        for i in root.grid_slaves(column=0,row=5):
            i.destroy()
        messageErr = ttk.Label(frm,text='Please select a text file after clicking the open file button')
        messageErr.grid(column=0,row=5)
    except UnicodeDecodeError: # Error gets raised if you try to convert a given file type and open it in the program, which raises the UnicodeDecodeError
        for i in root.grid_slaves(column=0,row=5):
            i.destroy()
        messageErr1 = ttk.Label(frm,text='Please select a text file')
        messageErr1.grid(column=0,row=5)
    
    

def down():
    if value.get() == 0:
        for i in root.grid_slaves(column=0,row=5):
            i.destroy()
        messageDown = ttk.Label(frm,text='Please Select Either Word Mode Or Character Mode')
        messageDown.grid(column=0,row=5)
    elif value.get() == 1:
        plot.bar(dictionary.keys(),dictionary.values())
        plot.savefig('graph.png')
        for i in root.grid_slaves(column=0,row=5):
            i.destroy()
        messageDown = ttk.Label(frm,text='Successfuly saved as \'graph.png\'!')
        messageDown.grid(column=0,row=5)
    elif value.get() == 2:
        plot.bar(char_dict.keys(),char_dict.values())
        plot.savefig('graph.png')
        for i in root.grid_slaves(column=0,row=5):
            print(i)
            i.destroy()
        messageDown = ttk.Label(frm,text='Successfuly saved as \'graph.png\'!')
        messageDown.grid(column=0,row=5)

# file = 0 # Creating a file variable that will allow the while loop to work
# while file == 0: # If the file variable doesnt get updated continue the loop, this allows the user to get unlimited attempts 
#     try:
#         global directory
#         directory = input('What is the file path of the text file?')
#         file = open(directory,'r')
#         initial_words = file.read().split()
#     except:
#         print('This file does not exist')



root = tkinter.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
value = tkinter.IntVar()
ttk.Radiobutton(frm,text='Word Mode',command=plot_words,value=1,variable=value).grid(column=0,row=1)
ttk.Radiobutton(frm,text='Character Mode',command=plot_chars,value=2,variable=value).grid(column=0,row=2)
ttk.Button(frm, text='Open File', command=create_var).grid(column=0,row=3)
ttk.Button(frm,text='Download', command=down).grid(column=0,row=4)
root.mainloop()
