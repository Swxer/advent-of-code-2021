f = open("input.txt", "r")

# part 1

horizontal = 0
depth = 0
for line in f:
  command = line.split(" ")
  if command[0] == "forward":
    horizontal += int(command[1])
  elif command[0] == "down":
    depth += int(command[1])
  elif command[0] == "up":
    depth -= int(command[1])

print(f"part 1 answer is {horizontal * depth}")

# part 2

f = open("input.txt", "r")
horizontal = 0
depth = 0
aim = 0
for line in f:
  command = line.split(" ")
  if command[0] == "forward":
    horizontal += int(command[1])
    depth += aim * int(command[1])
  elif command[0] == "down":
    aim += int(command[1])
  elif command[0] == "up":
    aim -= int(command[1])

print(f"part 2 answer is {horizontal * depth}")


