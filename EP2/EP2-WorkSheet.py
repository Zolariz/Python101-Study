from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox
import math

GUI = Tk()
GUI.title('โปรแกรมบันทึกผลการทดลอง')
GUI.geometry('1200x800')

######### Label ###############
L1 = Label(GUI, text='รายงานผลการทดลอง เรื่อง การไทเทรตกรด-เบส', font=('Angsana New',30), relief="groove", bg="white", fg='black')
L1.place(x=350, y=25)

GUI.columnconfigure(0, weight=1)
GUI.rowconfigure(0, weight=1)
######################################

L2 = Label(GUI, text='ตารางบันทึกผลการทดลอง', font=('Angsana New',20,"bold"), fg='black')
L2.place(x=100, y=100)

##################### Button1 #################################
FB1 = LabelFrame(GUI, text='การทดลองครั้งที่ 1', font=('Angsana New',16,"bold"))  # คล้ายกระดาน
FB1.place(x=100, y=150)

FBB1 = Label(FB1, text='ปริมาตรของ HCL (cm\u00b3)')
FBB1.grid(row=0, column=0,sticky='w',padx=10, pady=10)

# Create Entry widget
entry1 = ttk.Entry(FB1)
entry1.grid(row=0, column=1,padx=10, pady=10)

FBB2 = Label(FB1, text='ปริมาตรของ NaOH เริ่มต้น (cm\u00b3)')
FBB2.grid(row=1, column=0,sticky='w',padx=10, pady=10)

# Create Entry widget
entry2 = ttk.Entry(FB1)
entry2.grid(row=1, column=1,padx=10, pady=10)

FBB3 = Label(FB1, text='ปริมาตรของ NaOH สุดท้าย (cm\u00b3)')
FBB3.grid(row=2, column=0,sticky='w',padx=10, pady=10)

# Create Entry widget
entry3 = ttk.Entry(FB1)
entry3.grid(row=2, column=1,padx=10, pady=10)


# Function to retrieve the value entered in the Entry widget
def get_entry_value():
    value1 = (entry1.get())
    value2 = (entry2.get())
    value3 = (entry3.get())
    messagebox.showinfo('ปริมาตรสารละลายที่ใช้', 'ปริมาตรของ HCL ' + str(value1) + ' cm\u00b3\n'
                        'ปริมาตรของ NaOH เริ่มต้น ' + str(value2) + ' cm\u00b3\n'
                        'ปริมาตรของ NaOH สุดท้าย ' + str(value3) + ' cm\u00b3')

# Create button to retrieve the value
B1 = ttk.Button(FB1, text="Get Value", command=get_entry_value)
B1.grid(row=3, column=1,padx=10, pady=10)
###########################################################


##################### Button2 #################################
FB2 = LabelFrame(GUI, text='การทดลองครั้งที่ 2', font=('Angsana New',16,"bold"))  # คล้ายกระดาน
FB2.place(x=450, y=150)

FBB4 = Label(FB2, text='ปริมาตรของ HCL (cm\u00b3)')
FBB4.grid(row=0, column=0,sticky='w',padx=10, pady=10)

# Create Entry widget
entry4 = ttk.Entry(FB2)
entry4.grid(row=0, column=1,padx=10, pady=10)

FBB4 = Label(FB2, text='ปริมาตรของ NaOH เริ่มต้น (cm\u00b3)')
FBB4.grid(row=1, column=0,sticky='w',padx=10, pady=10)

# Create Entry widget
entry5 = ttk.Entry(FB2)
entry5.grid(row=1, column=1,padx=10, pady=10)

FBB5= Label(FB2, text='ปริมาตรของ NaOH สุดท้าย (cm\u00b3)')
FBB5.grid(row=2, column=0,sticky='w',padx=10, pady=10)

# Create Entry widget
entry6 = ttk.Entry(FB2)
entry6.grid(row=2, column=1,padx=10, pady=10)

# Function to retrieve the value entered in the Entry widget
def get_entry_value():
    value4 = entry4.get()
    value5 = entry5.get()
    value6 = entry6.get()
    messagebox.showinfo('ปริมาตรสารละลายที่ใช้', 'ปริมาตรของ HCL ' + str(value4) + ' cm\u00b3\n'
                        'ปริมาตรของ NaOH เริ่มต้น ' + str(value5) + ' cm\u00b3\n'
                        'ปริมาตรของ NaOH สุดท้าย ' + str(value6) + ' cm\u00b3')

# Create button to retrieve the value
B2 = ttk.Button(FB2, text="Get Value", command=get_entry_value)
B2.grid(row=3, column=1,padx=10, pady=10)
###########################################################

##################### Button3 #################################
FB3 = LabelFrame(GUI, text='การทดลองครั้งที่ 3', font=('Angsana New',16,"bold"))  # คล้ายกระดาน
FB3.place(x=800, y=150)

FBB7 = Label(FB3, text='ปริมาตรของ HCL (cm\u00b3)')
FBB7.grid(row=0, column=0,sticky='w',padx=10, pady=10)

# Create Entry widget
entry7 = ttk.Entry(FB3)
entry7.grid(row=0, column=1,padx=10, pady=10)

FBB8 = Label(FB3, text='ปริมาตรของ NaOH เริ่มต้น (cm\u00b3)')
FBB8.grid(row=1, column=0,sticky='w',padx=10, pady=10)

# Create Entry widget
entry8 = ttk.Entry(FB3)
entry8.grid(row=1, column=1,padx=10, pady=10)

FBB9 = Label(FB3, text='ปริมาตรของ NaOH สุดท้าย (cm\u00b3)')
FBB9.grid(row=2, column=0,sticky='w',padx=10, pady=10)

# Create Entry widget
entry9 = ttk.Entry(FB3)
entry9.grid(row=2, column=1,padx=10, pady=10)

# Function to retrieve the value entered in the Entry widget
def get_entry_value():
    value7 = entry7.get()
    value8 = entry8.get()
    value9 = entry9.get()
    messagebox.showinfo('ปริมาตรสารละลายที่ใช้', 'ปริมาตรของ HCL ' + str(value7) + ' cm\u00b3\n'
                        'ปริมาตรของ NaOH เริ่มต้น ' + str(value8) + ' cm\u00b3\n'
                        'ปริมาตรของ NaOH สุดท้าย ' + str(value9) + ' cm\u00b3')

# Create button to retrieve the value
B3 = ttk.Button(FB3, text="Get Value", command=get_entry_value)
B3.grid(row=3, column=1,padx=10, pady=10)
###########################################################


GUI.mainloop()