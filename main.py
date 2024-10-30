import tkinter as tk
from tkinter import ttk
import openpyxl

def load_data():
    path = r"C:\Users\PC\python_dev\book_data_management\book_data.xlsx"
    book_data = openpyxl.load_workbook(path)
    sheet = book_data.active
    
    list_value = list(sheet.values)
    print(list_value)
    for col_name in list_value[0]:
        treeview.heading(col_name, text=col_name)
        
    for value_tuple in list_value[1:]:
        treeview.insert("", tk.END, values=value_tuple)

def insert_row():
    bookname     = bookname_entry.get()
    authorname   = authorname_entry.get()
    price        = int(price_entry.get())
    status       = status_combobox.get()
    check_button = "済み" if a.get() else "未定"
    
    print(bookname, authorname, price, status, check_button)
    path = r"C:\Users\PC\python_dev\book_data_management\book_data.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active
    
    row_value = [bookname, authorname, price, status, check_button]
    sheet.append(row_value)
    workbook.save(path)
    
    #Insert row treeview
    treeview.insert('', tk.END, values=row_value)
    
#clear the values     
    bookname_entry.delete(0, "end")
    bookname_entry.insert(0, "書籍名")
    authorname_entry.delete(0, "end")
    authorname_entry.insert(0, "著者名")
    price_entry.delete(0, "end")
    price_entry.insert(0, "価格")
    status_combobox.set(combo_list[0])
    #check_button.state(["購入"])
    a.set(False)
    
    

def toggle_mode():
    if mode_switch.instate(["selected"]):
        
        style.theme_use("forest-dark")
    else:
        style.theme_use("forest-light")

root = tk.Tk() 
style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

combo_list = ["単行本", "Kindle"]

frame = ttk.Frame(root)
frame.pack()
widgets_frame = ttk.LabelFrame(frame, text="Inserrt Row")
widgets_frame.grid(row=0, column=0, padx=20, pady=10)

bookname_entry = ttk.Entry(widgets_frame)
bookname_entry.grid(row=0, column=0, padx=10, pady=10,sticky="w")
bookname_entry.insert(0,"書籍名")
bookname_entry.bind("<FocusIn>", lambda e: bookname_entry.delete(0, tk.END))

authorname_entry = ttk.Entry(widgets_frame)
authorname_entry.grid(row=1, column=0, padx=10, pady=10,sticky="w")
authorname_entry.insert(0,"著者名")
authorname_entry.bind("<FocusIn>", lambda e: authorname_entry.delete(0, tk.END))

price_entry = ttk.Entry(widgets_frame)
price_entry.grid(row=2, column=0, padx=10, pady=10,sticky="w")
price_entry.insert(0,"価格")
price_entry.bind("<FocusIn>", lambda e: price_entry.delete(0, tk.END))

status_combobox = ttk.Combobox(widgets_frame, values=combo_list)
status_combobox.current(0)
status_combobox.grid(row=3, column=0, padx=10, pady=10,sticky="w")

a=tk.BooleanVar()
check_button = ttk.Checkbutton(widgets_frame, text="購入", variable=a)
check_button.grid(row=4, column=0, padx=10, pady=10,sticky="nsew")

button = ttk.Button(widgets_frame, text="追加", command=insert_row)
button.grid(row=5, column=0, padx=10, pady=10,sticky="nsew")

separator = ttk.Separator(widgets_frame)
separator.grid(row=6, column=0, sticky="ew", padx=(20, 18), pady=10)

mode_switch = ttk.Checkbutton(
    widgets_frame, text="Mode", style="Switch", command=toggle_mode)
mode_switch.grid(row=7, column=0, padx=5, pady=10,sticky="nsew")

tree_frame = ttk.Frame(frame)
tree_frame.grid(row=0, column=1, pady=10)
treeScroll = ttk.Scrollbar(tree_frame)
treeScroll.pack(side="right", fill="y")

#リスト
cols = ("書籍名", "著者", "価格", "種類","購入")
treeview = ttk.Treeview(tree_frame, yscrollcommand=treeScroll.set, columns=cols, show="headings", height=13)

treeview.column("書籍名", width=400)
treeview.column("著者", width=200)
treeview.column("価格", width=100)
treeview.column("種類", width=100)
treeview.column("購入", width=100)
treeview.pack()
treeScroll.config(command= treeview.yview)

#データをロードする
load_data()

root.mainloop()