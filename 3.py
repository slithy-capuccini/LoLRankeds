import tkinter as tk
##read the txt and save in vavr
with open("games.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
    third_line=file.readline()
print(first_line)
first_line=first_line.strip()
print(second_line)
second_line=second_line.strip()
print(third_line)
third_line=third_line.strip()
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text + '\n'
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
def change_to_win(num_button):
    replace_line('games.txt',num_button,"Win")
##create tk
window = tk.Tk()
#create the button in normal is lose
button = tk.Button(
    text="Null",
    width=25,
    height=5,
    bg="#909090",
    fg="red",
    activebackground="#989595",
    command=change_to_win(0)
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
#same shit
button2 = tk.Button(
    text="Null",
    width=25,
    height=5,
    bg="#909090",
    fg="red",
    activebackground="#989595",
    command=change_to_win(1)
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
#same shit
button3 = tk.Button(
    text="Null",
    width=25,
    height=5,
    bg="#909090",
    fg="red",
    activebackground="#989595",
    command=change_to_win(2)
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
#mainloop
window.mainloop()
