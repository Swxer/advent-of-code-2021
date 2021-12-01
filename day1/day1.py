# open file
f = open("input.txt", "r")

# convert those numbers into list
l = [int(x) for x in f]

# part 1

# calculate the number of times measurement increases
firstTime = True
previousMeasurement = 0
counter = 0
for number in l:
  if firstTime:
    firstTime = False
  else:
    if number > previousMeasurement:
      counter += 1
  previousMeasurement = number

print(f"part 1 answer is {counter}")

# part 2
i = 2
firstTime = True
previousWindow = 0
counter = 0
while i < len(l):
  window = l[i] + l[i-1] + l[i-2]
  if firstTime:
    firstTime = False
  else:
    if window > previousWindow:
      counter += 1
  previousWindow = window

  i += 1
print(f"part 2 answer is {counter}")