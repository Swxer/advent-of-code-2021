f = open("input.txt", "r")

# part 1 answer is the first output
# part 2 answer is the last output

# the board will be represented using list of list
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]

# extract row numbers for the board
def extractRowNumbers(l):
  l = l.strip()
  l = l.split(" ")
  l = [n for n in l if n]
  return l

# make list of bingo boards
def extractListOfBingoBoards():
  numbers = [] 
  boards = []
  board = []
  firstLine = True
  rowCount = 0
  for line in f:
    # extract the drawing numbers first
    if firstLine:
      numbers = line
      firstLine = False
    else:
      # extact the bingo board
      if line != "\n":
        board.append(extractRowNumbers(line))
        rowCount += 1
      if rowCount == 5: 
      # 1 bingo board has been extracted, get another bingo board
        rowCount = 0
        boards.append(board)
        board = []
  return numbers, boards

# mark the boards with the drawn number
def markBoards(number, board):
  for row in range(len(board)):
    for col in range(len(board)):
      if board[row][col] == number:
        board[row][col] = "x"
  return board

# check if any bingo horizontally or vertically
def bingo(l):
  if all(element == "x" for element in l): return True
  return False

# calculate score
def printScore(board):
  totalScore = 0
  for row in range(len(board)):
      for col in range(len(board)):
        if board[row][col] != "x":
          totalScore += int(board[row][col])
  return totalScore

# check if theres any winner
def checkWinner(number, board):
  
  winner = False
  for row in range(len(board)):
    column = []
    for col in range(len(board)):
      column.append(board[col][row])

    # check vertically or horizontally
    if bingo(column) or bingo(board[row]): winner = True

  # BINGO!
  if winner: return True

# setting up the numbers and bingo boards
numbers, boards = extractListOfBingoBoards()
numbers = numbers.strip().split(",")

winner = []
# start playing lottery
for number in numbers:
  for i in range(len(boards)):
    boards[i] = markBoards(number, boards[i])
    if checkWinner(number, boards[i]) and i not in winner:
      if len(winner) == 0:
        print(f"the first winner is board no. {i+1} with score of {printScore(boards[i]) * int(number)}")
      elif len(boards) - len(winner) == 1:
        print(f"the last winner is board  no. {i+1} with score of {printScore(boards[i]) * int(number)}")
      winner.append(i)