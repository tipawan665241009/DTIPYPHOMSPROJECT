#เเสดงข้อมูลหลายๆ ประเภทใน pritn เดียว

#1. ใช้ , โดยที่จะมี space ในเเต่ละ ,
print("SAU" ,5555,123,456,True,10+50)

#2. ใช้ + มีข้อเเม้ ข้อมูลที่ไม่ใช้ String ต้องเเปลงเป็น sting เเละไม่มี spacให้เหมือนกลับ
print("SAU"+str(5555)+' '+str(123.456)+' '+str(True)+' 'str(10+50))

#3.ใช้เมธอดชื่อ format
print("SAU{} {} {} {}".format(555,123.465, True, 10+50))
print("SAU{} {} {} {}"format(555,123.465, True, 10+50))

#4. ใช้ f-string ****
print(f'SAU {5555} {123.456} {True} {10+50}')

#_ _ _ _ _ _ _ _ _
#กรณี 1 บรรทัดมีหลาย Statment ให้คั่นด้วย ;
print('aaa'); print(111); print(False)