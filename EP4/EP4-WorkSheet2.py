from tkinter import *
from tkinter import ttk  # theme of tk
from tkinter import messagebox
from datetime import datetime

############# CSV ################
import csv


def writecsv(datalist):
    with open('../EP4/data.csv', 'a', encoding='utf-8', newline='') as file:
        fw = csv.writer(file)  # fw = file writer
        fw.writerow(datalist)  # data-list = ['pen','pencil','eraser']


def readcsv():
    with open('../EP4/data.csv', encoding='utf-8', newline='') as file:
        fr = csv.reader(file)  # fr = file reader
        data = list(fr)
    return data


###################################

GUI = Tk()
GUI.title('โปรแกรมบันทึกผลการทดลอง')
GUI.geometry('1175x600')

######### Label ###############
L1 = Label(GUI, text='รายงานผลการทดลอง เรื่อง การไทเทรต กรด-เบส', font=('Angsana New',
                                                                       30), relief="groove", bg="white", fg='black')
L1.place(x=350, y=25)

GUI.columnconfigure(0, weight=1)
GUI.rowconfigure(0, weight=1)
######################################

L2 = Label(GUI, text='บันทึกผลการทดลอง', font=('Angsana New', 20, "bold"), fg='black')
L2.place(x=50, y=100)

##################### กล่องกรอกข้อมูล #################################
FB1 = LabelFrame(GUI, text='', font=('Angsana New', 16, "bold"))  # กล่องรวมด้านซ้าย
FB1.place(x=50, y=150)

FBB1 = Label(FB1, text='ปริมาตรของ HCL (cm\u00b3)')
FBB1.grid(row=0, column=0, sticky='w', padx=10, pady=10)

v_data1 = StringVar()  # ตัวแปรพิเศษที่ใช้กับข้อความใน GUI
E1 = ttk.Entry(FB1, textvariable=v_data1, font=('Angsana New', 20))
E1.grid(row=0, column=1, padx=20, pady=10)

FBB2 = Label(FB1, text='ปริมาตรของ NaOH เริ่มต้น (cm\u00b3)')
FBB2.grid(row=3, column=0, sticky='w', padx=10, pady=10)

v_data2 = StringVar()
E2 = ttk.Entry(FB1, textvariable=v_data2, font=('Angsana New', 20))
E2.grid(row=3, column=1, padx=20, pady=10)

FBB3 = Label(FB1, text='ปริมาตรของ NaOH สุดท้าย (cm\u00b3)')
FBB3.grid(row=5, column=0, sticky='w', padx=10, pady=10)

v_data3 = StringVar()
E3 = ttk.Entry(FB1, textvariable=v_data3, font=('Angsana New', 20))
E3.grid(row=5, column=1, padx=20, pady=10)

########################################

################## แสดง log ด้านขวา ###############################

FB2 = LabelFrame(GUI, text='', font=('Angsana New', 16, "bold"))  # กรอบรวมด้านขวามือ
FB2.place(x=500, y=150)

# Create a Text widget to display log messages
log_text = Text(FB2, font=('Angsana New', 16), height=10, width=80)
log_text.pack(pady=20, padx=25)

# Create a Scrollbar widget and attach it to the Text widget
scrollbar = ttk.Scrollbar(FB2, orient=VERTICAL, command=log_text.yview)
scrollbar.place(x=590, y=20, height=295)
log_text.config(yscrollcommand=scrollbar.set)

# Read data from CSV and insert into Text widget
data = readcsv()
for row in data:
    log_text.insert(END, "\n")
    log_text.insert(END, row)
    log_text.insert(END, "\n")


# Function to write data to CSV and insert into Text widget
def write_and_display():
    t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data1 = v_data1.get()
    data2 = v_data2.get()
    data3 = v_data3.get()
    text = [t, 'ปริมาตรของ HCL ' + data1 + ' cm\u00b3', 'ปริมาตรของ NaOH เริ่มต้น ' + data2 + ' cm\u00b3',
            'ปริมาตรของ NaOH สุดท้าย ' + data3 + ' cm\u00b3']
    writecsv(text)
    v_data1.set('')
    v_data2.set('')
    v_data3.set('')
    messagebox.showinfo('บันทึกข้อมูล', 'บันทึกข้อมูลเรียบร้อย')
    log_text.insert(END, "\n")  # แอดข้อมูลเพิ่มตรง log text
    log_text.insert(END, text)
    log_text.insert(END, "\n")


###############################################################

################# ปุ่มบันทึก ###################################
B1 = ttk.Button(FB1, text='บันทึก', command=write_and_display)
B1.grid(row=6, column=1, padx=10, pady=10)
##############################################################

GUI.mainloop()
