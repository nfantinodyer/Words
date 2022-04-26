import tkinter as tk
from english_words import english_words_lower_alpha_set
from random import choice
import re

window = tk.Tk()
window.title("Word Finder")
window.columnconfigure(0, weight=1,minsize=250)
window.rowconfigure(0, weight=1, minsize=250)



text_box = tk.Text(width=10, height=10)
ans = tk.Entry(width=11)

def clear():
    ans.config(state='normal')
    text_box.config(state='normal')
    text_box.delete(1.0, tk.END)
    ans.delete(0, tk.END)
    ans.config(state='disabled')
    text_box.config(state='disabled')


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

    #find all words that are in the known char list
    for i in range(len(cword)):
        letter = cword[i]
        for o in words:
            if re.search(letter, o):
                temp.append(o)
        words=temp
        temp=[]
    
    #removes words that are in the reject list
    for letter in reject:
        for word in words:
            if re.search(letter, word):
                continue
            else:
                temp.append(word)
        words=temp
        temp=[]
    
    x=len(words)
    ans.config(state='normal')
    ans.insert(0,str(x)+" results")
    print("The following "+str(x)+" words are "+str(length)+" letters long and contain the letters you entered: ")
    text_box.config(state='normal')
    for item in words:
        text_box.insert(tk.END, item+"\n")
    text_box.config(state='disabled')

    
    ans.pack(side = tk.BOTTOM, padx = 10, pady = 5)
    ans.config(state='disabled')




#llabel = tk.Label(text="Enter the length of the word you want to find: ")
#llabel.pack()

#l = tk.Entry(width=50)
#l.pack()



entrylabel = tk.Label(text="Enter the letters in the correct spots: ")
entrylabel.pack(side=tk.TOP,anchor=tk.W)

frame1 = tk.Frame(window, width=50, relief=tk.SUNKEN)
frame1.pack(fill=tk.X)

one = tk.Entry(frame1,width=3)
one.pack(side = tk.LEFT,padx=2,pady=5)

two = tk.Entry(frame1,width=3)
two.pack(side = tk.LEFT,padx=2,pady=5)

three = tk.Entry(frame1,width=3)
three.pack(side = tk.LEFT,padx=2,pady=5)

four = tk.Entry(frame1,width=3)
four.pack(side = tk.LEFT,padx=2,pady=5)

five = tk.Entry(frame1,width=3)
five.pack(side = tk.LEFT,padx=2,pady=5)


entrylabel = tk.Label(text="Enter the known letters: ")
entrylabel.pack(anchor=tk.W)

entryword = tk.Entry(width=20)
entryword.pack(anchor=tk.W,padx=2,pady=5)

rejectl = tk.Label(text="Enter the rejected letters: ")
rejectl.pack(anchor=tk.W)

reject = tk.Entry(width=20)
reject.pack(anchor=tk.W,pady=5,padx=2)

#int(l.get()) instead of 5
button = tk.Button(text="Search", width=10, height=2, command=lambda: check(5,one.get(), two.get(), three.get(), four.get(), five.get(),reject.get(), entryword.get()))
button.pack(anchor=tk.W,padx=2)

text_box.pack(side=tk.LEFT,padx=2,pady=5)
text_box.config(state='disabled')

def reset():
    clear()
    reject.delete(0, tk.END)
    entryword.delete(0, tk.END)
    one.delete(0, tk.END)
    two.delete(0, tk.END)
    three.delete(0, tk.END)
    four.delete(0, tk.END)
    five.delete(0, tk.END)


button = tk.Button(text="Exit", command=quit, width=10, height=2)
button.pack(side = tk.BOTTOM, padx=5, pady=5)

reset = tk.Button(text="Clear", width=10, height=2, command=reset)
reset.pack(side = tk.BOTTOM, padx=5, pady=5)






window.mainloop()