import tkinter

button_values = [
    ["AC", "±", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "±", "%", "√"]

row_count = len(button_values)
column_count = len(button_values[0])


color_teal = "#07fac7"
color_green = "#048a6e"
color_black = "#000000"
color_orange = "#FF9500"
color_white = "white"

#window setup
window = tkinter.Tk()
window.title("Ashraf's Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background =color_black,
                      foreground=color_white, anchor="e", width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range (column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30), 
                                width=column_count-1, height=1,
                                command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.configure(foreground=color_black, background=color_teal)
        elif value in right_symbols:
            button.configure(foreground=color_black, background=color_teal)
        else:
            button.configure(foreground=color_black, background=color_green)


        button.grid(row=row+1, column=column,)                   
        
frame.pack()

#A+B, A-B, A*C, A/C
A="0"
oparator = None
B = None

def clear_all():
    global A, B, oparator
    A = "0"
    oparator = None
    B = None

def remove_zeroe_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

def button_clicked(value):
    global right_symbols,top_symbols, A, B, oparator

    if value in right_symbols:
        if value == "=":
            if A is not None and oparator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)
                if oparator == "+":
                    label["text"] = remove_zeroe_decimal(numA + numB)
                elif oparator == "-":
                    label["text"] = remove_zeroe_decimal(numA - numB)
                elif oparator == "×":
                    label["text"] = remove_zeroe_decimal(numA * numB)
                elif oparator == "÷":
                    label["text"] = remove_zeroe_decimal(numA / numB)
           

                clear_all()
                    
        elif value in "÷×-+":
            if oparator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            oparator = value
            

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
            label["text"] = "0"

        elif value == "±":
            result = float(label["text"]) * -1
            label["text"] = remove_zeroe_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zeroe_decimal(result)
        elif value == "√":
            result = float(label["text"]) ** 0.5
            label["text"] = remove_zeroe_decimal(result)

    else:#digits or .
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value



window.mainloop()