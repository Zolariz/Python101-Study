import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import Customer_List

root = ttk.Window(themename='litera')
root.geometry("300x200")
root.title("โปรแกรมบันทึกรายชื่อ")

class MainApp(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("Customer List")
        self.geometry("800x600")

        self.customer_data = Customer_List.get_customer_data()

db = Customer_List.Database() # สร้าง object
rows = db.fetch() # เรียกใช้ method fetch() เพื่อดึงข้อมูล
db.insert("John", "john@example.com", 30, asdsadasdasd) # เรียกใช้ method insert() เพื่อเพิ่มข้อมูล
db.update(1, "John Doe", "johndoe@example.com", 35, qweasadasd) # เรียกใช้ method update() เพื่อแก้ไขข้อมูล

def change_theme():
    style = ttk.Style()
    if var.get():
        style.theme_use('darkly')
    else:
        style.theme_use('litera')
    label.configure(style='Primary.TLabel')

var = tk.BooleanVar()

check_button = ttk.Checkbutton(root, text="Dark Mode", var=var, bootstyle='light-round-toggle', command=change_theme)
check_button.pack(padx=10, pady=10)

# create a widget to show the style
label = ttk.Label(root, text='Hello, ttkbootstrap!', bootstyle='Primary.TLabel')
label.pack()

# start the application
root.mainloop()