
#!
# * โปรแกรมแสดงการทำงานของคำสั่งทำซ้ำ for ร่วมกับคำสั่ง continue
# * เพื่อพิมพ์ค่าในลิสต์
#!

color = ["red", "green"]
things = ["T-shirt", "skirt"]

for x in color:
    print("outer loop", x)
    for y in things:
        print("***inner loop***", y)
        print(x, y)
    print("")
