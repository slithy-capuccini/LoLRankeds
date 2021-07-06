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

##create tk
window = tk.Tk()
#create the button in normal is lose
button = tk.Button(
    text="Lose",
    width=25,
    height=5,
    bg="#ff0000",
    fg="yellow",
    activebackground="#e10000",
)
#change the button if is win
if first_line=="Win":
    button.configure(text="Win")
    button.configure(bg="#52eb00")  
    button.configure(activebackground="#49cc03")
button.pack()
#same shit
button2 = tk.Button(
    text="Lose",
    width=25,
    height=5,
    bg="#ff0000",
    fg="yellow",
    activebackground="#e10000",
)
#same shit
if second_line=="Win":
    button2.configure(text="Win")
    button2.configure(bg="#52eb00")  
    button2.configure(activebackground="#49cc03")
button2.pack()
#same shit
button3 = tk.Button(
    text="Lose",
    width=25,
    height=5,
    bg="#ff0000",
    fg="yellow",
    activebackground="#e10000",
)
#same shit
if third_line=="Win":
    button3.configure(text="Win")
    button3.configure(bg="#52eb00")  
    button3.configure(activebackground="#49cc03")
button3.pack()
#mainloop
window.mainloop()
