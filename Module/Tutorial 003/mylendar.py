import calendar
import checkday

d = calendar.weekday(2022, 1, 18)
print("วันที่ 18 มกราคม 2022 คือ ",
      checkday.checkdayofweek(d), "---> แทนด้วยเลข ", d)

d2 = calendar.firstweekday()
print(" วันแรกของสัปดาห์ คือ ", checkday.checkdayofweek(d2), "---> แทนด้วยเลข ", d2)

calendar.setfirstweekday(6)
d3 = calendar.firstweekday()
print(" วันแรกของสัปดาห์ คือ ", checkday.checkdayofweek(d3), "---> แทนด้วยเลข ", d3)

d4 = calendar.monthrange(2022, 12)
print("หา monthrange ของเดือนธันวาคม 2022 ผลคือ ",
      d4, "ดังนั้น วันแรกของเดือนนี้ คือ", checkday.checkdayofweek(d4[0]))
