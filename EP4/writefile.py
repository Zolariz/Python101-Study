# ชื่อโปรแกรม writefile.py

def writedata():    # แก้ไขไม่ได้
    with open('data.txt','w',encoding='utf-8') as file:
        file.write('สวัสดี')

def adddata(text):  # แก้ไขได้
    with open('add-data.txt','a',encoding='utf-8') as file:
        file.writelines(text + '\n')

def readdata():
    with open('add-data.txt',encoding='utf-8') as file:
        data = file.readlines() # export to list
        # data = file.read()
        print(data)

#adddata('ลูกชิ้น 20 บาท')
#adddata('ไส้กรอก 15 บาท')
#adddata('แซนวิช 10 บาท')

