from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox
from math import *

# สร้างหน้าต่าง GUI
root = Tk()
root.title("pH Calculator")
root.geometry('500x650')

L1 = Label(root, text='pH Calculator', font=('Angsana New',30))
L1.place(x=175, y=25)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

F1 = LabelFrame(root)
F1.place(x=175, y= 100)

FF1 = Label(F1, text='pH = -log [H⁺]', font=(30))
FF1.grid(row=0, column=0, sticky='nsew', padx= 10,pady=10)

# สร้าง label และ entry สำหรับการป้อนค่าของความอิ่มตัว
FB1 = LabelFrame(root)
FB1.place(x=50, y=180)

FBB1 = Label(FB1, text="ความเข้มข้น [H₃O⁺] (mol/L):")
FBB1.grid(row=0, column=0,sticky='w',padx=10, pady=10)

# Create Entry widget
entry1 = ttk.Entry(FB1)
entry1.grid(row=0, column=1,padx=10, pady=10)

# Function to retrieve the value entered in the Entry widget
def calculate_pH(concentration):
    # คำนวณ pH ตามสูตร
    pH = -log10(round(float(concentration), 2))
    return pH

def show_result():
    # รับค่าจากกล่องข้อความ
    concentration = entry1.get()
    result = calculate_pH(concentration)
    messagebox.showinfo('pH','ความเข้มข้น [H₃O⁺] ' + str(concentration) + 'mol/L\n'
                        'pH :' + str(result))

    # แสดงผลลัพธ์ใน label
    label_result.config(text="" + str(result))

# สร้างปุ่มสำหรับคำนวณ pH
button_calculate = ttk.Button(FB1, text="คำนวณ", command=show_result)
button_calculate.grid(row=1, column=2, padx=10, pady=10)

FBB2 = Label(FB1, text="pH : ")
FBB2.grid(row=1, column=0,sticky='e',padx=10, pady=10)

# สร้าง label สำหรับแสดงผลลัพธ์
label_result = Label(FB1, text="")
label_result.grid(row=1, column=1, padx=10, pady=10)
##############################################################

##################### pOH ###################################
F2 = LabelFrame(root)
F2.place(x=175, y= 300)

FF2 = Label(F2, text='pOH = -log [OH⁻]', font=(30))
FF2.grid(row=0, column=0, sticky='nsew', padx= 10,pady=10)

FF3 = Label(F2, text='pH = 14 - pH', font=(30))
FF3.grid(row=1, column=0, sticky='nsew', padx= 10,pady=10)

# สร้าง label และ entry สำหรับการป้อนค่าของความอิ่มตัว
FB2 = LabelFrame(root)
FB2.place(x=50, y=425)

FBB3 = Label(FB2, text="ความเข้มข้น [OH⁻] (mol/L):")
FBB3.grid(row=0, column=0,sticky='w',padx=10, pady=10)

# Create Entry widget
entry2 = ttk.Entry(FB2)
entry2.grid(row=0, column=1,padx=10, pady=10)

# Function to retrieve the value entered in the Entry widget
def calculate_pOH(concentration2):
    # คำนวณ pH ตามสูตร
    pOH = -log10(round(float(concentration2), 2))
    return pOH

def show_result2():
    # รับค่าจากกล่องข้อความ
    concentration2 = entry2.get()
    result2 = calculate_pOH(concentration2)

    label_result_2.config(text="" + str(result2))

    messagebox.showinfo('pOH','ความเข้มข้น [OH⁻] ' + str(concentration2) + 'mol/L\n'
                        'pOH :' + str(result2))
# สร้างปุ่มสำหรับคำนวณ pOH
button_calculate = ttk.Button(FB2, text="คำนวณ", command=show_result2)
button_calculate.grid(row=1, column=2, padx=10, pady=10)

FBB4 = Label(FB2, text="pOH : ")
FBB4.grid(row=1, column=0,sticky='e',padx=10, pady=10)

# สร้าง label สำหรับแสดงผลลัพธ์
label_result_2 = Label(FB2, text="")
label_result_2.grid(row=1, column=1, padx=10, pady=10)

def calculate_pH2(pOH):
    # คำนวณ pH ตามสูตร
    pH2 = 14 - pOH
    return pH2

def show_result3():
    # รับค่าจากกล่องข้อความ
    pOH = float(label_result_2["text"])
    result3 = calculate_pH2(pOH)
    # แสดงผลลัพธ์ใน label
    label_result3.config(text="" + str(result3))
    messagebox.showinfo('pH', 'pH ' + str(result3))

FBB5 = Label(FB2, text="pH : ")
FBB5.grid(row=2, column=0, sticky='e', padx=10, pady=10)

label_result3 = Label(FB2, text="")
label_result3.grid(row=2, column=1, padx=10, pady=10)

# สร้างปุ่มสำหรับคำนวณ pOH
button_calculate = ttk.Button(FB2, text="คำนวณ", command=show_result3)
button_calculate.grid(row=2, column=2, padx=10, pady=10)

F3 = LabelFrame(root, borderwidth=0)
F3.place(x=53, y= 560)

FF5 = Label(F3, text='--- หมายเหตุ = การคำนวน pH จาก pOH ต้องกดปุ่มคำนวน pOH ก่อนทุกครั้ง ---', borderwidth=0)
FF5.grid(row=0, column=0, sticky='nsew', padx= 10,pady=10)

root.mainloop()