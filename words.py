from english_words import english_words_lower_alpha_set
from random import choice
import re


def randomWord():
    return choice(english_words_lower_alpha_set)

def getWord():
    word=""
    letter=""
    while letter != ".":
        letter = input("Enter a letter: ")
        if letter != ".":
            word += letter
    return word



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
    print("The following "+str(x)+" words are "+length+" letters long and contain the letters you entered: ")
    for item in words:
        print(item)
            
        
length=input("Enter the length of the word you want to find: ")
check(length,getWord())




