import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import re

# win = tk.Tk()
win = ttk.Window(themename="solar")
win.title("Calculator")
win.geometry("300x450")
win.resizable(0,0)


# def numbers(num):
# #     outstring.set("")
# #     current_inp = outstring.get()
# #     outstring.set(current_inp + str(num))
#     current_text = outstring.get()

#     # Prevent starting with operator (except "-")
#     if current_text == "" and num in "+*/":
#         return

#     # Prevent multiple operators in a row
#     if current_text and current_text[-1] in "+-*/" and num in "+-*/":
#         return

#     outstring.set(current_text + num)

def numbers(num):
    current_text = outstring.get()

    # Prevent starting with +, *, /
    if current_text == "" and num in "+*/":
        return

    # Prevent multiple operators in a row (except allow - after * or /)
    if current_text:
        last_char = current_text[-1]

        # If last is operator and current is also operator
        if last_char in "+*/-" and num in "+*/-":
            # Only allow *- or /- (like -8*-5), but not ---, ++, etc.
            if last_char in "*/" and num == "-":
                outstring.set(current_text + num)
                return
            else:
                # Replace last operator with new one
                # BUT only if not ending with multiple operators already
                temp = re.sub(r'[+\-*/]+$', '', current_text)
                outstring.set(temp + num)
                return

    outstring.set(current_text + num)




def clears():
    global outstring
    outstring.set("")
    formul.set("")

def backspace():
    current = outstring.get()
    outstring.set(current[:-1])

def dot():
    current_text = outstring.get()
    num_list = re.split(r'[\+\-\*/]', current_text)  # Split on operators

    # अगर expression खाली है या नया number शुरू हो रहा है
    if current_text == "" or num_list[-1] == "":
        outstring.set(current_text + "0.")
    elif "." not in num_list[-1]:  # अगर आखिरी नंबर में पहले से dot नहीं है
        outstring.set(current_text + ".")

# def dot():
#     current_text = outstring.get()
#     num_list = re.split(r'[\+\-\*/]', current_text)  # Split on any operator
#     if "." not in num_list[-1]:  # Ensure last number does not have a dot
#         outstring.set(current_text + ".")

def percentage():
    current_text = outstring.get()
    if current_text:
        try:
            last_number = re.findall(r'\d+\.?\d*$', current_text)  # Find last number
            if last_number:
                updated_number = str(float(last_number[0]) / 100)
                new_text = re.sub(r'\d+\.?\d*$', updated_number, current_text)
                outstring.set(new_text)
        except:
            outstring.set("ERROR")


# def equaltot():
#     check = outstring.get()
#     if check:
#         formul.set(outstring.get())
#         try:
#             result = eval(check)
#             outstring.set(str(result))
#         except:
#             outstring.set("ERROR")
#             win.after(1500, clears)  # Clears "ERROR" after 1.5 second 


# def equaltot():
#     check = outstring.get()
#     if check:
#         formul.set(check)

#         try:
#             # Replace numbers with leading zeros (but not decimals) using regex
#             # Match standalone numbers (not part of decimal or expression like 0.5)
#             cleaned = re.sub(r'\b0+(\d+)', r'\1', check)
            
#             result = eval(cleaned)
#             outstring.set(str(result))
#         except:
#             outstring.set("ERROR")
#             win.after(1500, clears)

def equaltot():
    check = outstring.get()
    if check:
        # Remove trailing operator if exists
        if check[-1] in "+-*/":
            check = check[:-1]

        formul.set(check)

        try:
            # Remove leading zeros from numbers (like 0009 → 9)
            # cleaned = re.sub(r'\b0+(\d+)', r'\1', check)
            # cleaned = re.sub(r'(?<!\.)\b0+(\d+)', r'\1', check)
            cleaned = re.sub(r'\b0+(?=\d)', '', check)



            result = eval(cleaned)
            outstring.set(str(result))
        except:
            outstring.set("ERROR")
            win.after(1500, clears)


frame = tk.Frame(win, background="red")
outstring = tk.StringVar()
label1 = tk.Entry(frame, 
                  takefocus="0",
                  justify="right",
                  font=('Helvetica', 18), 
                  textvariable=outstring
                  )
formul = ttk.StringVar()
label2 = ttk.Label(frame, textvariable=formul, text = "Formula",font=('Helvetica', 14), anchor="e")

btn1 = ttk.Button(win, text="AC", command= clears)
btn2 = ttk.Button(win, text="%", command=percentage)
btn3 = ttk.Button(win, text="⌫", command=backspace)
btn4 = ttk.Button(win, text="÷", command=lambda: numbers("/"))

btn5 = ttk.Button(win, text="7", command=lambda: numbers("7"))
btn6 = ttk.Button(win, text="8", command=lambda: numbers("8"))
btn7 = ttk.Button(win, text="9", command=lambda: numbers("9"))
btn8 = ttk.Button(win, text="✖", command=lambda: numbers("*"))

btn9 = ttk.Button(win, text="4", command=lambda: numbers("4"))
btn10 = ttk.Button(win, text="5", command=lambda: numbers("5"))
btn11= ttk.Button(win, text="6", command=lambda: numbers("6"))
btn12 = ttk.Button(win, text="➖", command=lambda: numbers("-"))

btn13 = ttk.Button(win, text="1", command=lambda: numbers("1"))
btn14= ttk.Button(win, text="2", command=lambda: numbers("2"))
btn15= ttk.Button(win, text="3", command=lambda: numbers("3"))
btn16= ttk.Button(win, text="➕", command=lambda: numbers("+"))

btn17= ttk.Button(win, text="00", command=lambda: numbers("00"))
btn18= ttk.Button(win, text="0", command=lambda: numbers("0"))
btn19= ttk.Button(win, text=".", command=dot)
btn20= ttk.Button(win, text="=", command= equaltot)

win.columnconfigure((0,1,2,3), weight=1, uniform= "a")
win.rowconfigure((0,1,2,3,4,5), weight=1, uniform= "a")

frame.grid(row=0, column=0, columnspan=4, sticky="nsew")
frame.columnconfigure(0, weight=1, uniform="b")
frame.rowconfigure((0,1), weight=1, uniform="b")
# label2.pack(side="top", ipady=5)
# label1.pack(expand=True)
label2.grid(row=0, column=0, sticky="nsew", padx=5, pady=3)
label1.grid(row=1, column=0, sticky="nsew", padx=5, pady=3)

btn1.grid(row=1, column=0, sticky="nsew", padx=5, pady=6)
btn2.grid(row=1, column=1, sticky="nsew", padx=5, pady=6)
btn3.grid(row=1, column=2, sticky="nsew", padx=5, pady=6)
btn4.grid(row=1, column=3, sticky="nsew", padx=5, pady=6)

btn5.grid(row=2, column=0, sticky="nsew", padx=5, pady=6)
btn6.grid(row=2, column=1, sticky="nsew", padx=5, pady=6)
btn7.grid(row=2, column=2, sticky="nsew", padx=5, pady=6)
btn8.grid(row=2, column=3, sticky="nsew", padx=5, pady=6)

btn9.grid(row=3, column=0, sticky="nsew", padx=5, pady=6)
btn10.grid(row=3, column=1, sticky="nsew", padx=5, pady=6)
btn11.grid(row=3, column=2, sticky="nsew", padx=5, pady=6)
btn12.grid(row=3, column=3, sticky="nsew", padx=5, pady=6)

btn13.grid(row=4, column=0, sticky="nsew", padx=5, pady=6)
btn14.grid(row=4, column=1, sticky="nsew", padx=5, pady=6)
btn15.grid(row=4, column=2, sticky="nsew", padx=5, pady=6)
btn16.grid(row=4, column=3, sticky="nsew", padx=5, pady=6)

btn17.grid(row=5, column=0, sticky="nsew", padx=5, pady=6)
btn18.grid(row=5, column=1, sticky="nsew", padx=5, pady=6)
btn19.grid(row=5, column=2, sticky="nsew", padx=5, pady=6)
btn20.grid(row=5, column=3, sticky="nsew", padx=5, pady=6)

win.mainloop()