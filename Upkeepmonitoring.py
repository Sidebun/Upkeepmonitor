import tkinter as tk

r = tk.Tk() 
r.title('Upkeep monitor') 
r.geometry("800x600")
r.configure(bg="blue")
button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
button.pack() 
r.mainloop() 












