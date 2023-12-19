# Word Frequency Calculator 
import tkinter
from tkinter import ttk, filedialog
import matplotlib.pyplot as plot

msg_count = 0 # This variable is used to determine the rows and position number of custom messages (for error handling and the successful download message) 

def remove_punctuation(string): # when given a string this function will remove punctuation from the string, takes one parameter which should be a string
    ret = '' # The string that will be returned, new variable is created for concatenation purposes
    for i in string: # For loops through the string to look for alphabetic characters
        if i.lower() in 'abcdefghijklmnopqrstuvwxyz': # if current indexed letter is alphabetic then it will be concatenated to the end of the return var
            ret = ret + i.lower()
    return ret
def frequency(lis, word): # This function calculates the frequency of a string within a given list: this function takes two parameters one list and one string
    count = 0
    for i in lis: # iterates through the list
        if i == word: # each time the word is found in the list the count var increases
            count = count + 1
    return count/len(lis) # returns the appearances divided by the total word/character count
def remove_duplicates(lis): # Takes in one parameter, which should be a list and removes any elements that are repeated
    ret = list() # The list that will be returned
    for i in lis: # For loops through the list
        if i.lower() in ret: # If the word or char has already been added to the ret list the loop will skip to the next iteration (the duplicate won't be added to the new list twice)
            continue
        else:
            ret.append(i.lower()) # Appends the iteration variable if it is not a duplicate element
    return ret
def merge(lis1,lis2): # Takes in two lists as arguments and uses dictionary comprehension to marge the two into a dictionary
    return {lis1[n]:lis2[n] for n in range(len(lis1))} # This function will be called for simplicity reasons

def word_frequencies(string): # Takes in one parameter, purpose is to create a dictionary with the words as the keys and their frequencies as the value

    init_change = string.split() # Takes the string and splits it into a list, new element for each space so each element will be a different word
    words = list()
    no_dupe = list()
    for i in init_change: # for loops through the split list, takes out the punctuation, and appends it to the words list
        words.append(remove_punctuation(i))

    no_dupe = remove_duplicates(words) # Creates a new list that does not contain any duplicate words

    counts = list()
    for i in no_dupe: # for loops through the no_dupe list
        counts.append(frequency(words,i)) # appends the frequency of each word to the counts list, counts[0] is associated with no_dupe[0] and so on
    
    return merge(no_dupe,counts) # returns the merged dictionary of no_dupe and counts

def word_frequencies_stop(initial_words): # This function is similar to word_frequencies but excludes stop words
    init_change = initial_words.split()

    words = list()
    no_dupe = list()
    for i in init_change: # For loops through the split list and looks for words that are deemed as stop words
        if i.lower() in 'a an and are as at am be but by for if in is it no not of on or such that the their then there these they this to was will with':
            # The loop will skip to the next iteration if i is a stop word as defined in the string above
            continue
        else:
            words.append(remove_punctuation(i)) # if i is not a stop word it will be added to the words list, excluding punctuation

    no_dupe = remove_duplicates(words)

    counts = list()
    for i in no_dupe:
        counts.append(frequency(words,i))
    print(merge(no_dupe,counts))
    return merge(no_dupe,counts)

def char_frequencies(): # takes in no arguments, the purpose of this function is to create a dictionary with the char as the keys and the frequencies as the associated values
    chars = list(''.join(initial_words).lower()) # joins the list from the global variable together
    no_spc = list()
    for i in chars: # for loops through the joined string
        if i in 'abcdefghijklmnopqrstuvwxyz1234567890': # Appends i as long as its not considered whitespace to the no_spc list
            no_spc.append(i)
    no_dupe_chars = remove_duplicates(no_spc) # takes the filtered list and creates a list which excludes duplicates
    freqs = list()
    for i in no_dupe_chars: # for loops through the no_dupe_chars list
        freqs.append(frequency(no_spc,i)) # appends the frequency of each word to the counts list, freqs[0] is associated with no_dupe_chars[0] and so on
        
    return merge(no_dupe_chars,freqs)

    
def plot_words():
    global word_dict
    
    if check.get() == 1:
        word_dict = word_frequencies_stop(initial_words)
    else:
        word_dict = word_frequencies(initial_words)
    
    plot.bar(word_dict.keys(), word_dict.values())
    plot.xlabel('Words')  # Add x-axis label
    plot.ylabel('Frequency')  # Add y-axis label
    plot.show()

def plot_chars():
    plot.bar(char_dict.keys(), char_dict.values())
    plot.xlabel('Characters')  # Add x-axis label
    plot.ylabel('Frequency')  # Add y-axis label
    plot.show()

# Called when the 'Open File' button is clicked
def create_var(): # This function is mainly used for setup, it creates the global variable which contains the selected file's content
    global initial_words,word_dict,char_dict,msg_count
    try:
        file_path = filedialog.askopenfilename() # Asks the user to upload a file, opens the user's file explorer to select a file
        with open(file_path, 'r') as file: # goes into the text file the user gives and saves its content in the initial_words var
            initial_words = file.read()
        # Initially creates the plotting dictionary for both the character and word modes
        word_dict = word_frequencies(initial_words)
        char_dict = char_frequencies()
    except FileNotFoundError: # if the user closes out of the file selection or doesnot open a text file this error will be raised
        
        # The following line creates a label where the personalized error message is included, the msg_count variable allows the labels to follow a log format
        ttk.Label(frm,text=str(msg_count + 1) + '. Please select a text file after clicking the open file button').grid(column=0,row=msg_count+8) 
        msg_count = msg_count + 1 # Increases the count so the next label will get placed below and have different numbering

    except UnicodeDecodeError: # Error gets raised if you try to convert a given file type and open it in the program

        # The following line creates a label where the personalized error message is included, the msg_count variable allows the labels to follow a log format
        ttk.Label(frm,text=str(msg_count + 1) + '. Please select a text file').grid(column=0,row=msg_count+8)
        msg_count = msg_count + 1 # Increases the count so the next label will get placed below and have different numbering

# Function is called when the 'generate' button is clicked
def gen():
    global msg_count
    try:
        if value.get() == 0: # If the user did not select either word mode or character mode
            ttk.Label(frm,text=str(msg_count + 1) + '. Please Select Either Word Mode Or Character Mode').grid(column=0,row=msg_count+8) # Personalized message is added to the log
            msg_count = msg_count + 1 # Increases the count so the next label will get placed below and have different numbering
        elif value.get() == 1:
            plot_words() # if the mode selected is word mode then the bar graph for the words is created and shown
        elif value.get() == 2:
            plot_chars() # if the mode selected is character mode then the bar graph for the chars is created and shown
    except NameError: # if the user clicks generate before uploading a file then NameError is raised
        ttk.Label(frm,text=str(msg_count + 1) + '. Please Select A Text File Before Generating').grid(column=0,row=msg_count+8) # Personalized message is added to the log
        msg_count = msg_count + 1 # Increases the count so the next label will get placed below and have different numbering

# Function is called when the 'download' button is clicked
def down():
    global msg_count
    if value.get() == 0: # if the user clicks download without selecting a mode
        ttk.Label(frm,text=str(msg_count + 1) + '. Please Select Either Word Mode Or Character Mode').grid(column=0,row=msg_count+8) # Personalized message is added to the log
        msg_count = msg_count + 1 # Increases the count so the next label will get placed below and have different numbering
    elif value.get() == 1: # downloads the word bar graph
        plot.bar(word_dict.keys(),word_dict.values()) # Creates the graph to be downloaded
        plot.savefig('graph.png') # The command that actually downloads the graph
        ttk.Label(frm,text=str(msg_count + 1) + '. Successfuly saved as \'graph.png\'!').grid(column=0,row=msg_count+8) # Personalized message is added to the log
        msg_count = msg_count + 1 # Increases the count so the next label will get placed below and have different numbering
    elif value.get() == 2: # downloads the character bar graph
        plot.bar(char_dict.keys(),char_dict.values()) # Creates the graph to be downloaded
        plot.savefig('graph.png') # The command that actually downloads the graph
        ttk.Label(frm,text=str(msg_count + 1) + '. Successfuly saved as \'graph.png\'!').grid(column=0,row=msg_count+8) # Personalized message is added to the log
        msg_count = msg_count + 1 # Increases the count so the next label will get placed below and have different numbering



# The tkinter magic
        
# This code sets up the grid for the labels and buttons
root = tkinter.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
value = tkinter.IntVar() # Used to check whether character mode or word mode has been selected, 1 = word, 2 = char
check = tkinter.IntVar() # Used to check whether exclude stop words has been selected, 0 = no, 1 = yes

# The two labels is a reminder to the user
ttk.Label(frm,text='Reminder to close the graph window if you are changing preferences.').grid(column=0,row=0)
ttk.Label(frm,text='Not doing so may cause the graph to display incorrect information.').grid(column=0,row=1)

# These two radio buttons are used for mode selection, the value is stored in the value variable
ttk.Radiobutton(frm,text='Word Mode',value=1,variable=value).grid(column=0,row=2) 
ttk.Radiobutton(frm,text='Character Mode',value=2,variable=value).grid(column=0,row=3)

ttk.Checkbutton(frm,text='Exclude Stop Words',variable=check).grid(column=0,row=4) # This is used to determine whether or not the user wants to exclude stop words
ttk.Button(frm, text='Open File', command=create_var).grid(column=0,row=5) # gets the user to select the file, calls the create_var function when clicked
ttk.Button(frm,text='Generate', command=gen).grid(column=0,row=6) # when clicked the bar graph will generate and display, calls the gen function when clicked
ttk.Button(frm,text='Save graph as Image', command=down).grid(column=0,row=7) # when clicked the corresponding bar graph is downloaded to the user's computer, calls the down function when clicked

root.mainloop()
