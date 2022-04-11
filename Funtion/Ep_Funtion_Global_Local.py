
# * ขอบเขตของตัวแปร แบ่งออกได้เป็น 2 ปรเภท
# * Global Variable And Local Variable

# * แสดงการประกาศตัวแปรแบบ Global variable และ Local variable

from tkinter import Y


global_variable = 2


def local_variable(x):
    y = 4
    return x*y


result = global_variable * local_variable(3)

print("Result is ", result)
