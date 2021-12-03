import day1Data
import math

data = day1Data.data.split('\n')

for i, x in enumerate(data):
   data[i] = int(x)

class submarine():

    def __init__(self) -> None:
        pass

    def findFuel(self, mass) -> int:
        return math.trunc(mass/3) - 2

sub = submarine()

p1Sum = 0

for x in data:
    p1Sum += sub.findFuel(x)

print(p1Sum)
