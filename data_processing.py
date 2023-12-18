
# Word Frequency Calculator 
from tkinter import *
from tkinter import ttk
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

def plot_chars():
    plot.bar(char_dict.keys(),char_dict.values())
    plot.show()

file = 0 # Creating a file variable that will allow the while loop to work
while file == 0: # If the file variable doesnt get updated continue the loop, this allows the user to get unlimited attempts 
    try:
        file = open(input('What is the file path of the text file?'),'r')
        initial_words = file.read().split()
    except:
        print('This file does not exist')
dictionary = word_frequencies(initial_words)
char_dict = char_frequencies(initial_words)


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Radiobutton(frm,text='Word Mode',command=plot_words,value=1).grid(column=0,row=1)
ttk.Radiobutton(frm,text='Character Mode',command=plot_chars,value=2).grid(column=0,row=2)
root.mainloop()
file.close()
