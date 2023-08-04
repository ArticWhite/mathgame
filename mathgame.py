import tkinter as tk
import random
val1 = random.randint(1,600)
val2 = random.randint(1,600)
question = str(val1)+" + "+str(val2)
score = 0

#function for guessing number
def submitGuess():
    global val1
    global val2
    global score
    actual = val1+val2
    #print(str(entry.get())==str(actual))
    if (str(actual) == str(entry.get())):
        score+=1
        label_score.config(text= "score: "+str(score))
    val1 = random.randint(1,600)
    val2 = random.randint(1,600)
    question = str(val1)+" + "+str(val2)
    label_q.config(text= question)
    print(score)

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