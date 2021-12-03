from statistics import mode
from collections import Counter

f = open("input.txt", "r")
l = [binary.strip() for binary in f]

BINARY_LENGTH = len(l[0])

# part 1

i = 0
l = []
gamma = ""
while i < BINARY_LENGTH:
  # get common bit each digit from each number
  f.seek(0)
  for bit in f:
    l.append(bit[i])
  gamma += mode(l)
  l.clear()
  i += 1

epsilon = ""
for bit in gamma:
  # opposite binary of gamma
  if bit == "1":
    epsilon += "0"
  else:
    epsilon += "1"

print(f"part 1 answer is {int(gamma, 2) * int(epsilon, 2)}")

# part 2

# keep binary numbers that has x in yth digit
# read the challenge spec for more detail
def keepNumbers(bit, digit, z):
  x = []
  for binary in z:
    if bit == binary[digit]:
      x.append(binary)
  return x

# most common element
def mostFrequent(l):
  d = {}
  d.update(dict((i, l.count(i)) for i in l))
  if "1" in d.keys() and "0" in d.keys():
    if d["1"] >= d["0"]:
      return "1"
    else:
      return "0"
  elif "1" in d.keys() and "0" not in d.keys():
    return "1"
  else:
    return "0"

# least common element
def leastFrequent(l):
  d = {}
  d.update(dict((i, l.count(i)) for i in l))
  if "1" in d.keys() and "0" in d.keys():
    if d["1"] >= d["0"]:
      return "0"
    else:
      return "1"
  elif "1" in d.keys() and "0" not in d.keys():
    return "1"
  else:
    return "0"


def getRating(ratingType):
  a = []
  l = []
  i = 0
  # get common bit each digit from each number
  f.seek(0)
  for bit in f:
    l.append(bit[i])

  if ratingType == "oxygen":
    commonBit = mostFrequent(l)
  elif ratingType == "co2":
    commonBit = leastFrequent(l)

  f.seek(0)
  l.clear()
  l = [binary.strip() for binary in f]
  a = keepNumbers(commonBit, i, l)
  i += 1

  # for each new list, get the common bit in ith digit
  # update the last and repeat
  while len(a) > 1 or i < BINARY_LENGTH: 
    l.clear()
    for bit in a:
      l.append(bit[i])
    if ratingType == "oxygen":
      commonBit = mostFrequent(l)
    elif ratingType == "co2":
      commonBit = leastFrequent(l)
    a = keepNumbers(commonBit, i, a)
    i += 1
  return a[0]

oxygen = getRating("oxygen")
co2 = getRating("co2")

print(f"part 2 answer is {int(oxygen, 2) * int(co2, 2)}")



