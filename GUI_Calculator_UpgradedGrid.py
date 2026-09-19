import tkinter as tk

root = tk.Tk()
root.title("Upgraded GUI Calculator")

number=""
operator=""
firstnum=0
result=0

def add_number(n):
    global number
    number += str(n) 
    output.config(text=number)

def choose_operator(operate):
   global firstnum, operator, number
   if number:
      firstnum = float(number)
      operator = operate
      number = ""
      output.config(text=operator)

def calculate():
    global number, firstnum, operator, result
    if not number:
        return
    secondnum= float(number)
    if operator == "+":
      result = firstnum + secondnum
    elif operator == "-": 
      result = firstnum - secondnum
    elif operator == "*": 
        result = firstnum * secondnumgive
    elif operator == "/": 
       if secondnum == 0:
          output.config(text="Cannot divide by 0")
          return 
       result = firstnum / secondnum
    output.config(text=result)
    number = str(result)
    firstnum = 0
    operator = ""

def clear(): 
    global number, operator, firstnum, result
    number = ""
    operator = ""
    firstnum = 0
    result = 0
    output.config(text="OUTPUT")

tk.Button(root, text="➕", width=10,height=5,  command=lambda: choose_operator("+")).grid(row=1, column=4)
tk.Button(root, text="➖", width=10,height=5,  command=lambda: choose_operator("-")).grid(row=2, column=4)
tk.Button(root, text="➗", width=10,height=5,  command=lambda: choose_operator("/")).grid(row=3, column=4)
tk.Button(root, text="❌", width=10,height=5,  command=lambda: choose_operator("*")).grid(row=4, column=4)
tk.Button(root, text="1", width=10,height=5,  command=lambda: add_number(1)).grid(row=1, column=1)
tk.Button(root, text="2", width=10,height=5,  command=lambda: add_number(2)).grid(row=1, column=2)
tk.Button(root, text="3", width=10,height=5,  command=lambda: add_number(3)).grid(row=1, column=3)
tk.Button(root, text="4", width=10,height=5,  command=lambda: add_number(4)).grid(row=2, column=1)
tk.Button(root, text="5", width=10,height=5,  command=lambda: add_number(5)).grid(row=2, column=2)
tk.Button(root, text="6", width=10,height=5,  command=lambda: add_number(6)).grid(row=2, column=3)
tk.Button(root, text="7", width=10,height=5,  command=lambda: add_number(7)).grid(row=3, column=1)
tk.Button(root, text="8", width=10,height=5,  command=lambda: add_number(8)).grid(row=3, column=2)
tk.Button(root, text="9", width=10,height=5,  command=lambda: add_number(9)).grid(row=3, column=3)
tk.Button(root, text="0", height=5, command=lambda: add_number(0)).grid(row=4, column=0, columnspan=4,rowspan=1, sticky="ew",)
tk.Button(root, text="🟰", command=calculate, height=5, width=10).grid(row=4, column=4)
tk.Button(root, text="CLEAR", width=10, height=5, command=clear).grid(row=7, column=0, columnspan=5,rowspan=1, sticky="ew")

output = tk.Button(root, text="OUTPUT", height=5)
output.grid(row=6, column=0, columnspan=5, sticky="ew")

root.mainloop()
