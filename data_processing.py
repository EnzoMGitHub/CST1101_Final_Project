import os
from dotenv import load_dotenv

load_dotenv() 

# Functions
  
def occurances(word,lis):
    count = 0
    for i in lis:
        if i == word:
            count = count + 1
    return count

def remove_word(word,lis): # Work in progress
    ret = lis
    while word in ret:
        ret.remove(word)
    ret.append(word)
    return ret

# Data Processing
file = os.getenv("file")
f = open(file,'r')
lines = f.read()
lines = lines.split()

list_of_words = lines[:]
list_of_occurr = list()

 # Work in progress
# for i in lines:
#     if i.isalpha():
#         list_of_words = remove_word(i,list_of_words)
#         list_of_occurr.append(occurances(i,lines))
#     else:
#         new_word = ''
#         for j in i:
#             if j.isalpha():
#                 new_word = new_word + j
#         list_of_words = remove_word(i,list_of_words)
#         list_of_occurr.append(occurances(i,lines))
for i in lines:
    word = ''
    for j in i:
        if j.isalpha():
            word = word + j
    list_of_words = remove_word(i,list_of_words)
    list_of_occurr.append(occurances(i,lines))


print(lines)
print('No Dupe',list_of_words)
print(list_of_occurr)

f.close()