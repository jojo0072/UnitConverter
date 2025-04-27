import unit_data

import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Unit Converter")

lab_frame=tk.Frame(root)
lab_title=tk.Label(lab_frame, text="Unit Converter", font=("Hectiva", 15, "bold"))
lab_frame.pack()
lab_title.pack(padx=10, pady=10)

bottom_frame=tk.Frame(root)
bottom_frame.pack()

def choosen_size(*args):
    first_size=unit_data.categories[cat.get()]
    second_size=unit_data.categories[cat.get()]
    if cat.get()!="Temperature":
        first_unit_combobox["values"]=tuple(first_size.keys())
        second_unit_combobox["values"]=tuple(second_size.keys())
    else:
        first_unit_combobox["values"]=first_size
        second_unit_combobox["values"]=second_size

cat=tk.StringVar()
category_combobox=ttk.Combobox(bottom_frame, textvariable=cat, font=("Hectiva", 15))
category_combobox["values"]=tuple(unit_data.categories.keys())
category_combobox.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
cat.trace_add("write", choosen_size)

first_amount=tk.StringVar()
first_entry=tk.Entry(bottom_frame, textvariable=first_amount, font=("Hectiva", 15))
first_entry.grid(row=6, column=1, padx=10, pady=10)

first_unit=tk.StringVar()
first_unit_combobox=ttk.Combobox(bottom_frame, textvariable=first_unit, font=("Hectiva", 15))
first_unit_combobox.grid(row=6, column=2, padx=10, pady=10)

second_amount=tk.StringVar()
second_entry=tk.Entry(bottom_frame, textvariable=second_amount, font=("Hectiva", 15), state="readonly")
second_entry.grid(row=8, column=1, padx=10, pady=10)

second_unit=tk.StringVar()
second_unit_combobox=ttk.Combobox(bottom_frame, textvariable=second_unit, font=("Hectiva", 15))
second_unit_combobox.grid(row=8, column=2, padx=10, pady=10)

def is_float_int(num):
    try:
        int(num)
        return True
    except ValueError:
        try:
            float(num)
            return True
        except ValueError:
            return False

def check_conversion(*args):
    try:    
        if (is_float_int(first_amount.get())==True) and ((first_unit.get() and second_unit.get()) !=""):
                base=first_unit.get()
                target=second_unit.get()
                if cat.get() !="Temperature":
                    convert=float(first_amount.get())*(unit_data.categories[cat.get()][base]/unit_data.categories[cat.get()][target])
                else:
                    convert=unit_data.convert_temperature(float(first_amount.get()), base, target)

                return second_amount.set(convert)
    except KeyError:
        pass

first_amount.trace_add("write", check_conversion)
first_unit.trace_add("write",check_conversion)
second_unit.trace_add("write", check_conversion)

root.mainloop()