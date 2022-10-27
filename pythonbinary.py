userInput = input("Please enter a number: ")

remainder = 0
number = int(userInput)
binaryList = []
binary = ""

while number != 0:
    remainder = int(number % 2)
    binaryList.append(remainder)
    number = int(number / 2)

binaryList = binaryList[::-1]

for item in binaryList:
    binary += str(item)

print(binary)
