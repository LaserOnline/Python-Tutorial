
# * โปรแกรมแสดงการส่งข้อมูลไปยังฟังก์ชันแบบไม่จำกัดจำนวนข้อมูล

def myclass(*std_name):  # ? รับข้อมูลรายชื่อนักเรียน แบบไม่จำกัดจำนวน
    # ? หาค่าจำนวนข้อมูลทั้งหมดที่ส่งเข้ามายังฟังก์ชัน
    total_std = len(std_name)
    # ? อ้างอิงค่าข้อมูลของพารามิเตอร์ตัวแรก
    print("นักเรียนคนที่ 1 คือ ", std_name[0])
    # ? อ้างอิงค่าข้อมูลของพารามิเตอร์ตัวสุดท้าย
    print("นักเรียนคนสุดท้าย คือ ", std_name[total_std-1])


print("ห้อง 1/1")
myclass("นายดำ", "นายแดง", "นางเขียว", "นางสามชมพู")
print("ห้อง 1/2")
myclass("นายกล้วย", "นางสาวส้มเช้ง", "นางสาวเชอรี่", "นายองุ่น", "นางสาวลำไย")
