import tkinter as tk
##read the txt and save in vavr
with open("games5.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
    third_line=file.readline()
    fourth_line=file.readline()
    five_line=file.readline()
    last_day=file.readline()
first_line=first_line.strip()
second_line=second_line.strip()
third_line=third_line.strip()
fourth_line=fourth_line.strip()
five_line=five_line.strip()
last_day=last_day.strip()
print(last_day)
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text + '\n'
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
def change_to_win(event):
    replace_line('games5.txt',0,"Win")
    button.configure(text="Win")
    button.configure(bg="#52eb00") 
    button.configure(fg="yellow")
    button.configure(activebackground="#49cc03")
def change_to_win_2(event):
    replace_line('games5.txt',1,"Win")
    button2.configure(text="Win")
    button2.configure(bg="#52eb00") 
    button2.configure(fg="yellow")
    button2.configure(activebackground="#49cc03")
def change_to_win_3(event):
    replace_line('games5.txt',2,"Win")
    button3.configure(text="Win")
    button3.configure(bg="#52eb00") 
    button3.configure(fg="yellow")
    button3.configure(activebackground="#49cc03")
def change_to_win_4(event):
    replace_line('games5.txt',3,"Win")
    button4.configure(text="Win")
    button4.configure(bg="#52eb00") 
    button3.configure(fg="yellow")
    button3.configure(activebackground="#49cc03")
def change_to_win_5(event):
    replace_line('games5.txt',4,"Win")
    button5.configure(text="Win")
    button5.configure(bg="#52eb00") 
    button5.configure(fg="yellow")
    button5.configure(activebackground="#49cc03")
###Lose functions
def change_to_lose(event):
    replace_line('games5.txt',0,"Lose")
    button.configure(text="Lose")
    button.configure(bg="#ff0000")
    button.configure(fg="yellow")
    button.configure(activebackground="#e10000")
def change_to_lose_2(event):
    replace_line('games5.txt',1,"Lose")
    button2.configure(text="Lose")
    button2.configure(bg="#ff0000")
    button2.configure(fg="yellow")
    button2.configure(activebackground="#e10000")
def change_to_lose_3(event):
    replace_line('games5.txt',2,"Lose")
    button3.configure(text="Lose")
    button3.configure(bg="#ff0000")
    button3.configure(fg="yellow")
    button3.configure(activebackground="#e10000")
def change_to_lose_4(event):
    replace_line('games5.txt',3,"Lose")
    button4.configure(text="Lose")
    button4.configure(bg="#ff0000")
    button4.configure(fg="yellow")
    button4.configure(activebackground="#e10000")
def change_to_lose_5(event):
    replace_line('games5.txt',4,"Lose")
    button5.configure(text="Lose")
    button5.configure(bg="#ff0000")
    button5.configure(fg="yellow")
    button5.configure(activebackground="#e10000")
def reseteo():
    replace_line('games5.txt',0,"Null")
    replace_line('games5.txt',1,"Null")
    replace_line('games5.txt',2,"Null")
    replace_line('games5.txt',3,"Null")
    replace_line('games5.txt',4,"Null")
    button.configure(text="Null")
    button.configure(bg="#909090")
    button.configure(fg="red")
    button.configure(activebackground="#989595")
    button2.configure(text="Null")
    button2.configure(bg="#909090")
    button2.configure(fg="red")
    button2.configure(activebackground="#989595")
    button3.configure(text="Null")
    button3.configure(bg="#909090")
    button3.configure(fg="red")
    button3.configure(activebackground="#989595")
    button4.configure(text="Null")
    button4.configure(bg="#909090")
    button4.configure(fg="red")
    button4.configure(activebackground="#989595")
    button5.configure(text="Null")
    button5.configure(bg="#909090")
    button5.configure(fg="red")
    button5.configure(activebackground="#989595")
##create tk

window = tk.Tk()
#label of the last day
Label=tk.Label(window,text='Last day was:'+last_day)
Label.pack()
#create the button in normal is lose
button = tk.Button(
    text="Null",
    width=25,
    height=5,
    bg="#909090",
    fg="red",
    activebackground="#989595",
)
#change the button if is win
if first_line=="Win":
    button.configure(text="Win")
    button.configure(bg="#52eb00") 
    button.configure(fg="yellow")
    button.configure(activebackground="#49cc03")
elif first_line=="Lose":
    button.configure(text="Lose")
    button.configure(bg="#ff0000")
    button.configure(fg="yellow")
    button.configure(activebackground="#e10000")

button.pack()
button.bind('<Button-1>',change_to_win)
button.bind('<Button-3>',change_to_lose)
#same shit
button2 = tk.Button(
    text="Null",
    width=25,
    height=5,
    bg="#909090",
    fg="red",
    activebackground="#989595",
)
#change the button if is win
if second_line=="Win":
    button2.configure(text="Win")
    button2.configure(bg="#52eb00") 
    button2.configure(fg="yellow")
    button2.configure(activebackground="#49cc03")
elif second_line=="Lose":
    button2.configure(text="Lose")
    button2.configure(bg="#ff0000")
    button2.configure(fg="yellow")
    button2.configure(activebackground="#e10000")
button2.pack()
button2.bind('<Button-1>',change_to_win_2)
button2.bind('<Button-3>',change_to_lose_2)
#same shit
button3 = tk.Button(
    text="Null",
    width=25,
    height=5,
    bg="#909090",
    fg="red",
    activebackground="#989595",
)
#change the button if is win
if third_line=="Win":
    button3.configure(text="Win")
    button3.configure(bg="#52eb00") 
    button3.configure(fg="yellow")
    button3.configure(activebackground="#49cc03")
elif third_line=="Lose":
    button3.configure(text="Lose")
    button3.configure(bg="#ff0000")
    button3.configure(fg="yellow")
    button3.configure(activebackground="#e10000")
button3.pack()
button3.bind('<Button-1>',change_to_win_3)
button3.bind('<Button-3>',change_to_lose_3)
##samme shit
button4 = tk.Button(
    text="Null",
    width=25,
    height=5,
    bg="#909090",
    fg="red",
    activebackground="#989595",
)
#change the button if is win
if fourth_line=="Win":
    button4.configure(text="Win")
    button4.configure(bg="#52eb00") 
    button4.configure(fg="yellow")
    button4.configure(activebackground="#49cc03")
elif fourth_line=="Lose":
    button4.configure(text="Lose")
    button4.configure(bg="#ff0000")
    button4.configure(fg="yellow")
    button4.configure(activebackground="#e10000")
button4.pack()
button4.bind('<Button-1>',change_to_win_4)
button4.bind('<Button-3>',change_to_lose_4)
#same shit
button5 = tk.Button(
    text="Null",
    width=25,
    height=5,
    bg="#909090",
    fg="red",
    activebackground="#989595",
)
#change the button if is win
if five_line=="Win":
    button5.configure(text="Win")
    button5.configure(bg="#52eb00") 
    button5.configure(fg="yellow")
    button5.configure(activebackground="#49cc03")
elif five_line=="Lose":
    button5.configure(text="Lose")
    button5.configure(bg="#ff0000")
    button5.configure(fg="yellow")
    button5.configure(activebackground="#e10000")
button5.pack()
button5.bind('<Button-1>',change_to_win_5)
button5.bind('<Button-3>',change_to_lose_5)
#button of reset
button_reset = tk.Button(
    text="Reset",
    width=10,
    height=2,
    bg="#c7c7c7",
    activebackground="#bbbbbb",
    command=reseteo
)
button_reset.pack()
#new day 

#mainloop
window.mainloop()