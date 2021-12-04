import day3Data

data = day3Data.data.splitlines()

class binary():

    def __init__(self) -> None:
        self.zeros = 0 
        self.ones = 0
        self.gamma = ''
        self.oxy = ''
        self.co2 = ''

    def countEach(self, string : str, index : int) -> None:
        if (string[index] == '0'): self.zeros += 1
        elif (string[index] == '1'): self.ones += 1
    
    def createGamma(self) -> None:
        if(self.ones > self.zeros): self.gamma += '1'
        elif(self.zeros > self.ones): self.gamma += '0'

        #print("updating gamma... \n" + self.gamma)
        self.ones = 0 
        self.zeros = 0

    def binary2decimal(self, binary : str) -> int:
        return int(binary,2)
    
    def invertBinary(self, binary : str) -> str:
        #print("number to invert: \n"+ binary)
        inverse = ''
        for x in binary:
            if (x == '0'): inverse += '1'
            elif (x == '1'): inverse += '0'
            #print("updating inverse:\n" + inverse)
        
        return inverse

    def oxygenBit(self):
        if(self.ones > self.zeros or self.ones == self.zeros): self.oxy += '1'
        elif(self.zeros > self.ones): self.oxy += '0'

        self.ones = 0 
        self.zeros = 0

    def co2Bit(self):
        if(self.ones > self.zeros or self.ones == self.zeros): self.co2 += '0'
        elif(self.zeros > self.ones): self.co2 += '1'

        self.ones = 0 
        self.zeros = 0


gamma = binary()

y = 0

while (y < len(data[0])):
    for i, x in enumerate(data):
        gamma.countEach(x, y)
    gamma.createGamma()
    y += 1

gammaVal = gamma.binary2decimal(gamma.gamma)
epsilonVal = gamma.binary2decimal(gamma.invertBinary(gamma.gamma))

print(gammaVal)
print(epsilonVal)
print(gammaVal*epsilonVal)


oxyData = data

index = 0
while (len(oxyData) > 1):
    print(index)
    for x in oxyData:
        gamma.countEach(x, index)
    gamma.oxygenBit()
    for y in oxyData:
        if(y[index] != gamma.oxy[index]):
            print("removing stuff...") 
            oxyData.remove(y)
            print(oxyData)
    index += 1

print(oxyData)
    
