import day1Data # file w/given data for the problem

# creates a list of all the data points
data = day1Data.data.split('\n') # each number is on it's own line, so they're separated by newline char (\n)

for i, x in enumerate(data):
   data[i] = int(x) # converts each value in the list into a number


# part 1
def partOne(inData):
   increases = 0 # number of increases inbetween numbers

   for i, x in enumerate(inData):
      if (i == 0): # skip the first number b/c there isn't one before it to compare it to
          continue
      if x > data[i-1]: # if the current value is larger than the one before it, increase total
         increases += 1
   
   return increases # return total number of pairs where there was an increase

print(partOne(data))


# part 2
def partTwo(inData):
   increases = 0 # nunber of increases inbetween sums of the sets of three numbers

   for i, x in enumerate(inData):
      if (i+3 < len(inData)): # make sure to end 3 before the end so no issues w/data that doesn't exist
         # only need to compare current value and the value 3 indexes more --> other two values will be the same for the sums lol
         if (inData[i+3] > x): increases += 1

   return increases

print(partTwo(data))