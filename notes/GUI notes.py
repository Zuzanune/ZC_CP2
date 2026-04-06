import tkinter as tk

root = tk.Tk()

root.title("Testing GUI")
root.minsize(250, 250)
root.maxsize(1000, 1000)
root.geometry("300x300+100+100")
root.configure(background="Hot Pink")

start = tk.Label(root, text="This is a label", font=("Times New Roman", 30, "bold")).grid(row=0, column=0)
#start.config(fg="purple", background= 'Hot Pink').grid(row=0, column=0)
half = tk.Label(root, text="on my first GUI program", font=("Times New Roman", 10, "bold")).grid(row=1, column=0)
#half.config(fg="purple", background= 'Hot Pink').grid(row=1, column=0)

root.count = 0
def add():
    root.count += 1
    lbl['text'] = str(root.count)

def sub():
    root.count -= 1
    lbl['text'] = str(root.count)

btn = tk.Button(root, text= "add", command=add)
btn.grid(row= 4, column=0)
sbtn = tk.Button(root, text= "subtract", command=sub)
sbtn.grid(row= 4, column=1)
lbl = tk.Label(root, text= "0", font=("Times New Roman", 10))
lbl.grid(row=5, column=0, columnspan=2)
#lbl.config(fg="purple", background= 'Hot Pink').grid(row=5, column=0, columnspan=2)

close = tk.Button(root, text="close", command=root.destroy)
close.grid(row=6, column=0)
close.config(fg="purple", background= 'Hot Pink')
root.mainloop()


