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

    def oxygenBit(self) -> None:
        
        if(self.ones > self.zeros or self.ones == self.zeros): self.oxy += '1'
        elif(self.zeros > self.ones): self.oxy += '0'

        self.ones = 0 
        self.zeros = 0

    def co2Bit(self) -> None:
        if(self.ones > self.zeros or self.ones == self.zeros): self.co2 += '0'
        elif(self.zeros > self.ones): self.co2 += '1'

        self.ones = 0 
        self.zeros = 0

class partTwo():

    def __init__(self, inData):
        self.oxygen = inData
        self.CO2 = inData
        
    def keepMostCommonOxy(self, index : int) -> None:
        values = {'1' : 0, '0' : 0}

        for x in self.oxygen:
            values[x[index]] += 1

        mostCommon = ('1' if values['1'] >= values['0'] else '0')
        
        toReturn = []
        
        for x in range(0, len(self.oxygen)):
            if self.oxygen[x][index] != mostCommon:
                toReturn.append(self.oxygen[x])

        self.oxygen = toReturn
    
    def KeepLeastCommonCO2(self, index : int) -> None:
        values = {'1' : 0, '0' : 0}

        for x in self.CO2:
            values[x[index]] += 1

        leastCommon = ('1' if values['1'] < values['0'] else '0')

        toReturn = []
        
        for x in range(0, len(self.CO2)):
            if self.CO2[x][index] != leastCommon:
                toReturn.append(self.CO2[x])

        self.CO2 = toReturn

    def getFinalOxyVal(self) -> int:
        index = 0 
        while (len(self.oxygen) > 1):
            self.keepMostCommonOxy(index)
            index += 1

        return self.binaryToDecimal(self.oxygen[0])

    def getFinalCO2Val(self) -> int:
        index = 0
        while (len(self.CO2) > 1):
            self.KeepLeastCommonCO2(index)
            index += 1
        
        return self.binaryToDecimal(self.CO2[0])
        
    def binaryToDecimal(self, binary : str) -> int:
        total = 0
        binary = list(binary)
        binary.reverse()
        for index, digit in enumerate(binary):
            total += (2 ** index) * int(digit)

        return total

    def getFinalVal(self) -> int:
        return self.getFinalCO2Val() * self.getFinalOxyVal()
            
oxyData = data

partTwoStatic = partTwo(oxyData)

print(partTwoStatic.getFinalVal())


"""
gamma = binary()

# part 1
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


# part 2
'''oxyData = data

index = 0
while (len(oxyData) > 1): 
    print(index)
    gamma.mostCommon()
    gamma.oxygenBit()
    for y in oxyData:
        if(y[index] != gamma.oxy[index]):
            #print("removing stuff...") 
            oxyData.remove(y)
            #print(oxyData)
    index += 1

print(oxyData)'''
"""