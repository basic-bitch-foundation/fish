import tkinter as tk 
root = tk.Tk()

root.title("fish")

root.geometry("400x400")


fish = tk.Label(root, text="text")
x =0
y =0

def move():
    
    global x,y 
    x += 10
    y += 10
    fish.place(x=x,y=y)
    fish.after(30,move)
    

    
    

    
move()

root.mainloop()







