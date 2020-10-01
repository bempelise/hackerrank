from math import atan
from math import pi

AB = int(input())
BC = int(input())
TAN = AB/BC
DEGREE_SIGN = u'\N{DEGREE SIGN}'
THETA = atan(TAN)*180/pi
print(str(round(THETA)) + DEGREE_SIGN)
