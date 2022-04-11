
# *  def ชื่อฟังก์ชัน(พารามิเตอร์ตัวที่ 1, พารามิเตอร์ตัวที่ 2 = default, พารามิเตอร์ตัวสุดท้าย = default ):
# *     คำสั่งการทำงานต่างๆ ภายในฟังก์ชัน

# * โปรแกรมแสดงการทำงานของพารามิเตอร์ที่มีค่า default
# * ร่วมกับพารามิเตอร์ที่ไม่่มีค่า default

def information(age, nationalty="ไทย", status="โสด"):
    print("ฉันสัญชาติ"+nationalty+"อายุ"+str(age)+"สถานภาพ"+status)


information(30, "\t")
information(40, "อังกฤษ \t")
information(50, "ออสเตรเลีย \t", "สมรส")
