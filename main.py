

file = open("C:/Users/schule/Downloads/AOC/AOC/2/test.txt", 'r')

input = file.readlines()

finalRed = 12
finalGreen = 13
finalBlue = 14

final = 0
valid = False

for line in input:

    lineDeleter1 = line.replace(";", ",")
    lineDeleter2 = lineDeleter1.replace(":", ",")
    row = lineDeleter2.split(", ")

    for element in row:
        id = row[0].find(element[5])

print(id)

               
                        

                


