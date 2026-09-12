import tkinter as tk

root = tk.Tk()
root.title("GUI Calculator")

print("GUI Calculator:")
num1=int(input("Enter a number: "))
result=num1

def on_addclick():
    num2=int(input("Enter another number: "))
    result=int(num1+num2)
    print(result)

def on_subclick():
     num2=int(input("Enter another number: "))
     result=int(num1-num2)
     print(result)

lbl = tk.Label(root, text="Add")
lbl.grid(row = 0, column = 0)

btn = tk.Button(root, text="+", command=on_addclick)
btn.grid(row = 0, column = 1)

lbl = tk.Label(root, text="Subtract")
lbl.grid(row = 1, column = 0)

btn = tk.Button(root, text="-", command=on_subclick)
btn.grid(row = 1, column = 1)

root.mainloop()
  