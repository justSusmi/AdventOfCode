file = open('input.txt','r')

input = file.readlines()

chars = "abcdefghijklmnopqrstuvw"

nums = []
newLine = ""
final = 0
counter = 0
finalString = ""

for line in input:
    for x in line:
        if x.isdigit():
            counter+=1
    if counter == 1:
        final += x*11

    for y in line:
        if y.isdigit():
            nums.append(y)

    finalString = nums[0] + nums[len(nums)-1]
    final += int(finalString)
    nums.clear()
    print(final)
