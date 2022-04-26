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
ans = tk.Entry()

def clear():
    text_box.delete(1.0, tk.END)
    ans.delete(0, tk.END)


def check(length, one, two, three, four, five, reject, cword):
    clear()
    words=[]
    temp=[]
    letters = [one, two, three, four, five]
    start=0

    #until first letter is found
    for i in range(length):
        if letters[i] != "":
            start=i
            break

    #find all words that start with the first letter
    for item in english_words_lower_alpha_set:
        if len(item) == int(length):
            letter = letters[start]
            if re.match(letter, item[start]):
                words.append(item)
    start+=1

    #find all words that start with the remaining letters
    for i in range(length-start):
        for word in words:
            letter = letters[start+i]
            if re.match(letter, word[start+i]):
                temp.append(word)
            
        words=temp
        temp=[]

    for i in range(len(cword)):
        letter = cword[i]
        for o in words:
            if re.search(letter, o):
                temp.append(o)
        words=temp
        temp=[]
    
    if len(words) == 0:
        text_box.insert(tk.END, "No words found")
        return

    for letter in reject:
        for word in words:
            if re.search(letter, word):
                continue
            else:
                temp.append(word)
        words=temp
        temp=[]
    
    x=len(words)
    ans.insert(0,str(x)+" results")
    print("The following "+str(x)+" words are "+str(length)+" letters long and contain the letters you entered: ")
    for item in words:
        text_box.insert(tk.END, item+"\n")
    ans.pack()


#llabel = tk.Label(text="Enter the length of the word you want to find: ")
#llabel.pack()

#l = tk.Entry(width=50)
#l.pack()



entrylabel = tk.Label(text="Enter the letters in the correct spots: ")
entrylabel.pack(side = tk.LEFT)

one = tk.Entry(width=3)
one.pack(side = tk.LEFT)

two = tk.Entry(width=3)
two.pack(side = tk.LEFT)

three = tk.Entry(width=3)
three.pack(side = tk.LEFT)

four = tk.Entry(width=3)
four.pack(side = tk.LEFT)

five = tk.Entry(width=3)
five.pack(side = tk.LEFT)

entrylabel = tk.Label(text="Enter the known letters: ")
entrylabel.pack()

entryword = tk.Entry(width=50)
entryword.pack()

rejectl = tk.Label(text="Enter the rejected letters: ")
rejectl.pack()

reject = tk.Entry(width=50)
reject.pack()


#int(l.get()) instead of 5
button = tk.Button(text="Search", width=10, height=2, command=lambda: check(5,one.get(), two.get(), three.get(), four.get(), five.get(),reject.get(), entryword.get()))
button.pack()

text_box.pack()

button = tk.Button(text="Exit", command=quit, width=10, height=2)
button.pack()




window.mainloop()