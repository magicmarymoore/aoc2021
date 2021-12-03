import day2Data # file w/given data for the problem

# creates a list of all the data points
data = day2Data.data.splitlines()


class drive():

    def __init__(self) -> None:
        self.horizontal = 0 # horizontal movement of the submarine -> forward
        self.vertical = 0 # vertical movement of the submarine -> up/down
        self.aim = 0 # aim of the submarine, from part 2

    # part 1 move function
    def move(self, direction : str, magnitude : int):
        if direction == "forward":
            self.horizontal += magnitude # adjust the horizontal movement
        elif direction == "down":
            self.vertical += magnitude # adjust the vertical movement
        elif direction == "up":
            self.vertical -= magnitude # adjust the vertical movement

    # split up element into the direction and magnitude components
    def splitString(self, string : str) -> list:
        split = string.split(' ') # there is a space inbetween the direction and magnitude
        return [split[0], int(split[1])]

    # part 2 move function
    def move2(self, direction : str, magnitude : int):
        if direction == "forward":
            self.horizontal += magnitude # adjust the horizontal movement
            self.vertical += self.aim * magnitude # adjust the vertical movement
        elif direction == "down":
            self.aim += magnitude # adjust the aim
        elif direction == "up":
            self.aim -= magnitude # adjust the aim


x = drive()

for a in data:
    b = x.splitString(a) # split it up into direction and magnitude
    x.move2(b[0], b[1]) # move the correct way (change move2() to move() to solve part 1...)

print(x.horizontal, x.vertical) # the horizontal and vertical components the submarine has moved
print(x.horizontal * x.vertical) # multiply them together to find total distance traveled

