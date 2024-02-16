import math

x, y = 0, 0      # 칠 공 좌표
a, b = 0, 1     # 넣을 공 좌표

if x-a < 0:
    angle = 90 - math.degrees(math.atan((y-b)/(x-a)))
elif x-a > 0:
    angle = 270 - math.degrees(math.atan((y - b) / (x - a)))
else:       # 0이면 ㄴㄴㄴㄴ
    angle = None

print(angle)