
# !
# * เราสามารถนำคำสั่งทำซ้ำ for มาช้อนกันได้ โดยคำสั่งทำ for
# * ที่อยู่ด้านใน เรียกว่า inner loop
# * และ คำสั่งทำซ้ำ for ที่อยู่ด้านนอก เรียกว่า outer loop
# !
color = ["red", "green", "blue", "yellow"]
things = ["shirt", "skirt"]

for x in color:
    for y in things:
        print(x, "==", y)
