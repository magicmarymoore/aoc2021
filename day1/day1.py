import day1Data

data = day1Data.data.split('\n')

for i, x in enumerate(data):
   data[i] = int(x)

def partOne(inData):
   increases = 0
   for i, x in enumerate(inData):
      if (i == 0):
          continue
      if x > data[i-1]:
         increases += 1
   
   return increases

print(partOne(data))

def partTwo(inData):
   increases = 0

   for i, x in enumerate(inData):
      if (i+3 < len(inData)):
         if (inData[i+3] > x): increases += 1

   return increases

print(partTwo(data))