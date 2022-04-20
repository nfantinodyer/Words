import tkinter as tk
from english_words import english_words_lower_alpha_set
from random import choice
import re

window = tk.Tk()
window.title("Word Finder")
window.columnconfigure(0, weight=1,minsize=250)
window.rowconfigure(0, weight=1, minsize=250)

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

text_box = tk.Text(width=50, height=10)

def check(length,word):
    words=[]
    temp=[]
    
    for item in english_words_lower_alpha_set:
        if len(item) == int(length):
            letter = word[0]
            if re.search(letter, item):
                words.append(item)
            for i in range(len(word)-1):
                letter = word[i+1]
                for o in words:
                    if re.search(letter, o):
                        temp.append(o)
                words=temp
                temp=[]
   
    x=len(words)
    print("The following "+str(x)+" words are "+str(length)+" letters long and contain the letters you entered: ")
    for item in words:
        text_box.insert(tk.END, item+"\n")


llabel = tk.Label(text="Enter the length of the word you want to find: ")
llabel.pack()

l = tk.Entry(width=50)
l.pack()

entrylabel = tk.Label(text="Enter the known letters: ")
entrylabel.pack()

entry = tk.Entry(width=50)
entry.pack()


button = tk.Button(text="Search", width=10, height=2, command=lambda: check(int(l.get()),entry.get()))
button.pack()

text_box.pack()


button = tk.Button(text="Exit", command=quit, width=10, height=2)
button.pack()




window.mainloop()