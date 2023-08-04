import tkinter as tk
import random
val1 = random.randint(1,600)
val2 = random.randint(1,600)
typeQuestion = random.randint(1,3)
if (typeQuestion==1):
    question = str(val1)+" + "+str(val2)
elif (typeQuestion == 2):
    question = str(val1)+" - "+str(val2)
else:
    question = str(val1)+" x "+str(val2)
score = 0

#function for guessing number
def submitGuess():
    global val1
    global val2
    global score
    global typeQuestion
    if(typeQuestion==1):
        actual = val1+val2
    elif(typeQuestion==2):
        actual = val1-val2
    else:
        actual = val1*val2
    if (str(actual) == str(entry.get())):
        score+=1
        label_score.config(text= "score: "+str(score))
    val1 = random.randint(1,600)
    val2 = random.randint(1,600)
    typeQuestion = random.randint(1,3)
    question = str(val1)+" + "+str(val2)
    if (typeQuestion==1):
        question = str(val1)+" + "+str(val2)
    elif (typeQuestion == 2):
        question = str(val1)+" - "+str(val2)
    else:
        question = str(val1)+" x "+str(val2)
    label_q.config(text= question)
    entry.config(text="")

window = tk.Tk()

title_lbl = tk.Label(text="math game")
title_lbl.pack()
#question prompt
label_q = tk.Label(text = question)
label_q.pack()

label_score = tk.Label(text ="score: "+str(score))
label_score.pack()
button = tk.Button(
text="submit guess!",
width=25,
height=2,
command=submitGuess, 
bg="blue",
fg="yellow",
)
button.pack()
entry = tk.Entry()
entry.pack()
window.mainloop()