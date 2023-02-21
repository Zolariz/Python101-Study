# list กับ dictionary

box = []
box.append('ปากกา') # เพิ่มข้อมูลเข้าไปในกล่องๆนึงที่มีความคล้ายกัน
box.append('ดินสอ')
box.append('ยางลบ')

print(box)
print(box[1])
print(box[0])

brand = {'pen':['Lamy','Pentel','Fiber-Castle'],'pencil':['horse','steidler'],'eraser':'ยางลบ2สี'}

print(brand['pen'][1])
print(brand['pencil'][0])
print(brand.values())