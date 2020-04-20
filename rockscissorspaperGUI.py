#import library
import random
import tkinter as tk

#create window
window = tk.Tk()
window.geometry("400x300")
window.title("ROCK SCISSOR PAPER GAME")

#global variables
#score set into zero
user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""

#definition function methods for convert user choice
def choice_to_number(choice):
    rsp = {'rock':0,'scissor':1,'paper':2}
    return rsp[choice]
def number_to_choice(number):
    rsp = {0:'rock',1:'scissor',2:'paper'}
    return rsp[number]

#function for computer's choice
#use random
def random_computer_choice():
    return random.choice(['rock','scissor','paper'])

#result function
def result(human_choice,comp_choice):
    global user_score
    global comp_score
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user == comp):
        print("Tie")
    elif ((user-comp)%3==1):
        print("you win!!!")
        user_score += 1
    else:
        print("comp win!")
        comp_score += 1
    text_area = tk.Text(master=window, height=12, width=30, bg="#4cbbb9")
    text_area.grid(column=0, row=4)
    answer = "User Choice: {uc} \n Computer Choice : {cc} \n User Score : {u} \n Computer Score : {c} ".format(uc=user_choice, cc=comp_choice, u=user_score, c=comp_score)
    text_area.insert(tk.END,answer)

#function method for 3 different user choices
#for generate computer choice
def rock():
    global user_choice
    global comp_choice
    user_choice = 'rock'
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)
def scissor():
    global user_choice
    global comp_choice
    user_choice = 'scissor'
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)
def paper():
    global user_choice
    global comp_choice
    user_choice = 'paper'
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

#create button
button1 = tk.Button(text ="       Rock      ",bg="#fcf7bb",command = rock)
button1.grid(column=0, row=1)
button2 = tk.Button(text ="      Scissor    ",bg="#7f78d2",command = scissor)
button2.grid(column=0, row=2)
button3 = tk.Button(text ="       Paper     ",bg="#ffd3b6",command = paper)
button3.grid(column=0, row=3)

window.mainloop()