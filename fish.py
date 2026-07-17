import tkinter as tk 
root = tk.Tk()

root.title("fish")

root.geometry("400x400")


fish = tk.Label(root, text="text")
x =0
y =0

for i in range(10):
    fish.place(x = x, y= y)
    y = y + 10
    x =  x +10
    fish.place(x =x , y=y)
    

    
   



  

    



    
    
   
root.mainloop()







