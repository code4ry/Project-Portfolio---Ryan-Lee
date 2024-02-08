import random

ICON_Red = '\033[0;31;41m X \033[0;0m' #colors and shape
ICON_Blue = '\033[0;31;46m O \033[0;0m' #colors and shape
global continued

numPositions = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 "] # list that makes board for players to use as a map

positions = [ICON_Red, ICON_Red, ICON_Red, "   ", "   ", "   ", ICON_Blue, ICON_Blue, ICON_Blue] # list that puts red on top row, empty middle row and blue bottom row
                                                                                                ## positions will be utilized as it is the gameboard that changes as the game is played


def gameboard(positionList): ### makes boards with pieces
  print (positionList[0]  + "|" + positionList[1] + "|" + positionList[2]) 
  print ("-----------")
  print (positionList[3]  + "|" + positionList[4] + "|" + positionList[5])
  print ("-----------")
  print (positionList[6]  + "|" + positionList[7] + "|" + positionList[8])
  print("") #prints board with pieces

def ai_moves(line): ### initializes text file code and allows for AI to learn
  file1 = open("AI_moves.txt", "r")
  textInfo = file1.readlines()
  file1.close()
  newInfo = textInfo[line][0:len(textInfo[line])-1]
  listString = []
  for n in newInfo:
    listString.append(n)
  for n in listString:
    if n == '\n':
      listString.remove('\n')
  
  return listString ## returns a string

def ai_learn(line, answer):
  file1 = open("AI_moves.txt", "r")
  textInfo = file1.readlines()
  file1.close()
  newInfo = textInfo[line][0:len(textInfo[line])]
  listString = []
  for n in newInfo:
    listString.append(n)
  if Win == False and continued == False:
    listString.remove(str(answer))
  elif Win == True and continued == False:
    listString.append(str(answer))
  theString = ""
  for n in listString:
    theString += n
  textInfo[line] = theString
  finalString = ""
  for n in textInfo:
    finalString += n
  file = open("info.txt", "w")
  file.write(finalString[:-1]) 
  file.close()


def moveValid(turn, answer, positions, piece): ### giant function that determines how the piece move on the board and what's allowed for both player 1 and the computer
  if turn == 1: ### code that allows for player 1 to move
    temp = positions[int(piece) - 1]
    positions[int(piece) - 1] = positions[int(answer) - 1]
    positions[int(answer) - 1] = temp
    return positions
  if turn == 2:  ### conditions for computer and scenerios it can take on turn 2
    if positions == [ICON_Red, ICON_Red, ICON_Red, ICON_Blue, "   ", "   ", "   ", ICON_Blue, ICON_Blue]:
      line = 2
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = [ICON_Red, "   ", ICON_Red, ICON_Red, "   ", "   ", "   ", ICON_Blue, ICON_Blue]
      elif answer == 2:
        positions = [ICON_Red, "   ", ICON_Red, ICON_Blue, ICON_Red, "   ", "   ", ICON_Blue, ICON_Blue]
      elif answer == 3:
        positions = [ICON_Red, ICON_Red, "   ", ICON_Blue, "   ", ICON_Red, "   ", ICON_Blue, ICON_Blue]
    elif positions == [ICON_Red, ICON_Red, ICON_Red, "   ", ICON_Blue, "   ", ICON_Blue, "   ", ICON_Blue]:
      line = 3
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", ICON_Red, ICON_Red, "   ", ICON_Red, "   ", ICON_Blue, "   ", ICON_Blue]
      elif answer == 2:
        positions = ["   ", ICON_Red, ICON_Red, ICON_Red, ICON_Blue, "   ", ICON_Blue, "   ", ICON_Blue]
      elif answer == 3:
        positions = [ICON_Red, ICON_Red, "   ", "   ", ICON_Blue, ICON_Red, ICON_Blue, "   ", ICON_Blue]
      elif answer == 4:
        positions = [ICON_Red, ICON_Red, "   ", "   ", ICON_Blue, ICON_Red, ICON_Blue, "   ", ICON_Blue]
    elif positions == [ICON_Red, ICON_Red, ICON_Red, "   ", "   ", ICON_Blue, ICON_Blue, ICON_Blue, "   "]:
      line = 4
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", ICON_Red, ICON_Red, ICON_Red, "   ", ICON_Blue, ICON_Blue, ICON_Blue, "   "]
      elif answer == 2:
        positions = [ICON_Red, "   ", ICON_Red, "   ", ICON_Red, ICON_Blue, ICON_Blue, ICON_Blue, "   "]
      elif answer == 3:
        positions = [ICON_Red, "   ", ICON_Red, "   ", "   ", ICON_Red, ICON_Blue, ICON_Blue, "   "]
    return positions
  if turn == 3: ### code that allows for player 1 to move around
    if positions[int(answer) - 1] != "   ":
      positions[int(answer)  - 1] = ICON_Blue
      positions[int(answer) - 1] = positions[int(piece) - 1]
      positions[int(piece) - 1] = "   "
    else:
      temp = positions[int(piece) - 1]
      positions[int(piece) - 1] = positions[int(answer) - 1]
      positions[int(answer) - 1] = temp
    return positions
  if turn == 4:  ### conditions for computer and scenerios it can take on turn 4
    if positions == [ICON_Red, "   ", ICON_Red, ICON_Red, ICON_Blue, "   ", "   ", "   ", ICON_Blue]:
      line = 6
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = [ICON_Red, "   ", ICON_Red, "   ", ICON_Blue, "   ", ICON_Red, "   ", ICON_Blue]
      elif answer == 2:
        positions = ["   ", "   ", ICON_Red, ICON_Red, ICON_Red, "   ", "   ", "   ", ICON_Blue]
      elif answer == 3:
        positions = [ICON_Red, "   ", "   ", ICON_Red, ICON_Red, "   ", "   ", "   ", ICON_Blue]
      elif answer == 4:
        positions = [ICON_Red, "   ", "   ", ICON_Red, ICON_Blue, ICON_Red, "   ", "   ", ICON_Blue]
    elif positions == [ICON_Red, "   ", ICON_Red, "   ", ICON_Blue, ICON_Red, ICON_Blue, "   ", "   "]:
      line = 7
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", "   ", ICON_Red, ICON_Red, ICON_Blue, ICON_Red, ICON_Blue, "   ", "   "]
      elif answer == 2:
        positions = ["   ", "   ", ICON_Red, "   ", ICON_Red, ICON_Red, ICON_Blue, "   ", "   "]
      elif answer == 3:
        positions = [ICON_Red, "   ", "   ", "   ", ICON_Red, ICON_Red, ICON_Blue, "   ", "   "]
      elif answer == 4:
        positions = [ICON_Red, "   ", ICON_Red, "   ", ICON_Blue, "   ", ICON_Blue, "   ", ICON_Red]
    elif positions == ["   ", ICON_Red, ICON_Red, ICON_Blue, ICON_Red, "   ", "   ", "   ", ICON_Blue]:
      line = 8
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", "   ", ICON_Red, ICON_Red, ICON_Red, "   ", "   ", "   ", ICON_Blue]
      elif answer == 2:
        positions = ["   ", ICON_Red, ICON_Red, ICON_Blue, "   ", "   ", "   ", ICON_Red, ICON_Blue]
      elif answer == 3:
        positions = ["   ", ICON_Red, ICON_Red, ICON_Blue, "   ", "   ", "   ", "   ", ICON_Red]
      elif answer == 4:
        positions = ["   ", ICON_Red, "   ", ICON_Blue, ICON_Red, ICON_Red, "   ", "   ", ICON_Blue]
    elif positions == [ICON_Red, "   ", ICON_Red, ICON_Blue, ICON_Blue, "   ", "   ", ICON_Blue, "   "]:
      line = 9
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", "   ", ICON_Red, ICON_Blue, ICON_Red, "   ", "   ", ICON_Blue, "   "]
      elif answer == 2:
        positions = [ICON_Red, "   ", "   ", ICON_Blue, ICON_Red, "   ", "   ", ICON_Blue, "   "]
      elif answer == 3:
        positions = [ICON_Red, "   ", "   ", ICON_Blue, ICON_Blue, ICON_Red, "   ", ICON_Blue, "   "]
    elif positions == [ICON_Red, "   ", ICON_Red, "   ", ICON_Blue, ICON_Blue, "   ", ICON_Blue, "   "]:
      line = 10
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", "   ", ICON_Red, ICON_Red, ICON_Blue, ICON_Blue, "   ", ICON_Blue, "   "]
      elif answer == 2:
        positions = ["   ", "   ", ICON_Red, "   ", ICON_Red, ICON_Blue, "   ", ICON_Blue, "   "]
      elif answer == 3:
        positions = [ICON_Red, "   ", "   ", "   ", ICON_Red, ICON_Blue, "   ", ICON_Blue, "   "]
    elif positions == [ICON_Red, ICON_Red, "   ", ICON_Blue, "   ", ICON_Blue, "   ", "   ", ICON_Blue]:
      line = 11
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = [ICON_Red, "   ", "   ", ICON_Red, "   ", ICON_Blue, "   ", "   ", ICON_Blue]
      elif answer == 2:
        positions = [ICON_Red, "   ", "   ", ICON_Blue, ICON_Red, ICON_Blue, "   ", "   ", ICON_Blue]
      elif answer == 3:
        positions = [ICON_Red, "   ", "   ", ICON_Blue, "   ", ICON_Red, "   ", "   ", ICON_Blue]
    elif positions == ["   ", ICON_Red, ICON_Red, ICON_Blue, "   ", ICON_Blue, ICON_Blue, "   ", "   "]:
      line = 12
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = [ICON_Red, "   ", "   ", ICON_Red, "   ", ICON_Blue, "   ", "   ", ICON_Blue]
      elif answer == 2:
        positions = [ICON_Red, "   ", "   ", ICON_Blue, ICON_Red, ICON_Blue, "   ", "   ", ICON_Blue]
      elif answer == 3:
        positions = [ICON_Red, "   ", "   ", ICON_Blue, "   ", ICON_Red, "   ", "   ", ICON_Blue]
    elif positions == ["   ", ICON_Red, ICON_Red, "   ", ICON_Red, ICON_Blue, ICON_Blue, "   ", "   "]:
      line = 13
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", ICON_Red, ICON_Red, "   ", "   ", ICON_Blue, ICON_Red, "   ", "   "]
      elif answer == 2:
        positions = ["   ", ICON_Red, ICON_Red, "   ", "   ", ICON_Blue, ICON_Blue, ICON_Red, "   "]
      elif answer == 3:
        positions = ["   ", "   ", ICON_Red, "   ", ICON_Red, ICON_Red, ICON_Blue, "   ", "   "]
    elif positions == ["   ", ICON_Red, ICON_Red, ICON_Red, ICON_Blue, ICON_Blue, ICON_Blue, "   ", "   "]:
      line = 14
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", "   ", ICON_Red, ICON_Red, ICON_Blue, ICON_Red, ICON_Blue, "   ", "   "]
      elif answer == 2:
        positions = ["   ", ICON_Red, "   ", ICON_Red, ICON_Red, ICON_Blue, ICON_Blue, "   ", "   "]
    elif positions == [ICON_Red, "   ", ICON_Red, ICON_Red, "   ", ICON_Blue, "   ", ICON_Blue, "   "]:
      line = 15
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = [ICON_Red, "   ", ICON_Red, "   ", "   ", ICON_Blue, ICON_Red, ICON_Blue, "   "]
      elif answer == 2:
        positions = [ICON_Red, "   ", ICON_Red, "   ", "   ", ICON_Blue, "   ", ICON_Red, "   "]
    elif positions == [ICON_Red, "   ", ICON_Red, ICON_Blue, "   ", ICON_Red, "   ", ICON_Blue, "   "]:
      line = 16
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = [ICON_Red, "   ", ICON_Red, ICON_Blue, "   ", "   ", "   ", ICON_Red, "   "]
      elif answer == 2:
        positions = [ICON_Red, "   ", ICON_Red, ICON_Blue, "   ", "   ", "   ", ICON_Blue, ICON_Red]
    elif positions == [ICON_Red, ICON_Red, "   ", ICON_Blue, ICON_Blue, ICON_Red, "   ", "   ", ICON_Blue]:
      line = 17
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", ICON_Red, "   ", ICON_Blue, ICON_Red, ICON_Red, "   ", "   ", ICON_Blue]
      elif answer == 2:
        positions = [ICON_Red, "   ", "   ", ICON_Red, ICON_Blue, ICON_Red, "   ", "   ", ICON_Blue]
    elif positions == ["   ", ICON_Red, ICON_Red, "   ", ICON_Blue, "   ", "   ", "   ", ICON_Blue]:
      line = 18
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", ICON_Red, "   ", "   ", ICON_Red, "   ", "   ", "   ", ICON_Blue]
      elif answer == 2:
        positions = ["   ", ICON_Red, "   ", "   ", ICON_Blue, ICON_Red, "   ", "   ", ICON_Blue]
    elif positions == ["   ", ICON_Red, ICON_Red, "   ", ICON_Blue, "   ", ICON_Blue, "   ", "   "]:
      line = 19
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", ICON_Red, "   ", "   ", ICON_Red, "   ", ICON_Blue, "   ", "   "]
      elif answer == 2:
        positions = ["   ", ICON_Red, "   ", "   ", ICON_Blue, ICON_Red, ICON_Blue, "   ", "   "]
    elif positions == [ICON_Red, "   ", ICON_Red, ICON_Blue, "   ", "   ", "   ", "   ", ICON_Blue]:
      line = 20
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = [ICON_Red, "   ", "   ", ICON_Blue, "   ", ICON_Red, "   ", "   ", ICON_Blue]
    return positions
  if turn == 5: ### code that allows player 1 to move on turn 5
    if positions[int(answer) - 1] != "   ":
      positions[int(answer)  - 1] = ICON_Blue
      positions[int(answer) - 1] = positions[int(piece) - 1]
      positions[int(piece) - 1] = "   "
    else:
      temp = positions[int(piece) - 1]
      positions[int(piece) - 1] = positions[int(answer) - 1]
      positions[int(answer) - 1] = temp
    return positions
  if turn == 6: ### conditions for computer and scenerios it can take on turn 6
    if positions == ["   ", "   ", ICON_Red, ICON_Red, ICON_Red, ICON_Blue, "   ", "   ", "   "]:
      line = 22
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", "   ", ICON_Red, "   ", ICON_Red, ICON_Blue, ICON_Red, "   ", "   "]
      elif answer == 2:
        positions = ["   ", "   ", ICON_Red, ICON_Red, "   ", ICON_Blue, "   ", ICON_Red, "   "]
    elif positions == [ICON_Red, "   ", "   ", ICON_Blue, ICON_Blue, ICON_Blue, "   ", "   ", "   "]:
      line = 23
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", "   ", "   ", ICON_Blue, ICON_Red, ICON_Blue, "   ", "   ", "   "]
    elif positions == ["   ", ICON_Red, "   ", ICON_Red, ICON_Blue, ICON_Blue, "   ", "   ", "   "]:
      line = 24
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", ICON_Red, "   ", "   ", ICON_Blue, ICON_Blue, ICON_Red, "   ", "   "]
      elif answer == 2:
        positions = ["   ", "   ", "   ", ICON_Red, ICON_Blue, ICON_Red, "   ", "   ", "   "]
    elif positions == ["   ", ICON_Red, "   ", ICON_Blue, ICON_Blue, ICON_Red, "   ", "   ", "   "]:
      line = 25
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", "   ", "   ", ICON_Red, ICON_Blue, ICON_Red, "   ", "   ", "   "]
      elif answer == 2:
        positions = ["   ", ICON_Red, "   ", ICON_Blue, ICON_Blue, "   ", "   ", "   ", ICON_Red]
    elif positions == [ICON_Red, "   ", "   ", ICON_Red, ICON_Red, ICON_Blue, "   ", "   ", "   "]:
      line = 26
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = [ICON_Red, "   ", "   ", "   ", ICON_Red, ICON_Blue, ICON_Red, "   ", "   "]
      elif answer == 2:
        positions = [ICON_Red, "   ", "   ", ICON_Red, "   ", ICON_Blue, "   ", ICON_Red, "   "]
    elif positions == ["   ", "   ", ICON_Red, ICON_Blue, ICON_Red, ICON_Red, "   ", "   ", "   "]:
      line = 27
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", "   ", ICON_Red, ICON_Blue, "   ", ICON_Red, "   ", ICON_Red, "   "]
      elif answer == 2:
        positions = ["   ", "   ", ICON_Red, ICON_Blue, ICON_Red, "   ", "   ", "   ", ICON_Red]
    elif positions == ["   ", "   ", ICON_Red, ICON_Red, ICON_Blue, "   ", "   ", "   ", "   "]:
      line = 28
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", "   ", ICON_Red, "   ", ICON_Blue, "   ", ICON_Red, "   ", "   "]
      elif answer == 2:
        positions == ["   ", "   ", "   ", ICON_Red, ICON_Red, "   ", "   ", "   ", "   "]
      elif answer == 3:
        positions = ["   ", "   ", "   ", ICON_Red, ICON_Blue, ICON_Red, "   ", "   ", "   "]
    elif positions == ["   ", ICON_Red, "   ", ICON_Blue, ICON_Red, "   ", "   ", "   ", "   "]:
      line = 29
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", "   ", "   ", ICON_Red, ICON_Red, "   ", "   ", "   ", "   "]
      elif answer == 2:
        positions = ["   ", ICON_Red, "   ", ICON_Blue, "   ", "   ", "   ", ICON_Red, "   "]
    elif positions == ["   ", ICON_Red, "   ", "   ", ICON_Red, ICON_Blue, "   ", "   ", "   "]:
      line = 30
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", ICON_Red, "   ", "   ", "   ", ICON_Blue, "   ", ICON_Red, "   "]
      elif answer == 2:
        positions = ["   ", "   ", "   ", "   ", ICON_Red, ICON_Red, "   ", "   ", "   "]
    elif positions == [ICON_Red, "   ", "   ", ICON_Red, ICON_Blue, "   ", "   ", "   ", "   "]:
      line = 31
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = [ICON_Red, "   ", "   ", "   ", ICON_Blue, "   ", ICON_Red, "   ", "   "]
      elif answer == 2:
        positions = ["   ", "   ", "   ", ICON_Red, ICON_Red, "   ", "   ", "   ", "   "]
    elif positions == ["   ", "   ", ICON_Red, "   ", ICON_Blue, ICON_Red, "   ", "   ", "   "]:
      line = 32
      choices = ai_moves(line)
      answer = (random.choice(choices))
      answer = int(answer)
      if answer == 1:
        positions = ["   ", "   ", "   ", "   ", ICON_Red, ICON_Red, "   ", "   ", "   "]
      elif answer == 2:
        positions = ["   ", "   ", ICON_Red, "   ", ICON_Blue, "   ", "   ", "   ", ICON_Red]
    return positions
  if turn == 7: ### code that allows for player 1 to move
    if positions[int(answer) - 1] != "   ":
      positions[int(answer)  - 1] = ICON_Blue
      positions[int(answer) - 1] = positions[int(piece) - 1]
      positions[int(piece) - 1] = "   "
    else:
      temp = positions[int(piece) - 1]
      positions[int(piece) - 1] = positions[int(answer) - 1]
      positions[int(answer) - 1] = temp
  return positions, line, answer

def winCon(turn, positions): ### win conditions for stalemates and when the piece gets to the other side
  li = []
  turn = str(turn)
  for i in range(positions.count(ICON_Blue)):
    index = positions.index(ICON_Blue)
    li.append(index)
  for index in li: ### checks board for any stalemates
    if index == 0:
      if turn in "357":
        continued = False

    elif index == 1:
      if turn in "357":
        continued = False

    elif index == 2:
      if turn in "357":
        continued = False
    
    elif index == 3:
      if positions[index-3] == "   ":
        continued = True
      elif positions[index-2] == ICON_Red:
        continued = True
      else:
        continued = False

    elif index == 4:
      if positions[index-4] == ICON_Red:
        continued = True
      elif positions[index-3] == "   ":
        continued = True
      elif positions[index-2] == ICON_Red:
        continued = True
      else:
        continued = False

    elif index == 5:
      if positions[index-3] == "   ":
        continued = True
      elif positions[index-4] == ICON_Red:
        continued = True
      else:
        continued = False

    elif index == 6:
      if positions[index-3] == "   ":
        continued = True
      elif positions[index-2] == ICON_Red:
        continued = True
      else:
        continued = False
      
    elif index == 7:
      if positions[index-4] == ICON_Red:
        continued = True
      elif positions[index-3] == "   ":
        continued = True
      elif positions[index-2] == ICON_Red:
        continued = True
      else:
        continued = False
      
    elif index == 8:
      if positions[index-3] == "   ":
        continued = True
      elif positions[index-4] == ICON_Red:
        continued = True
      else:
        continued = False
      
  return continued
  
gameboard(numPositions) #print number map
print ("")
gameboard(positions) #print real board

turn = 0
line = 0
match = 1
continued = True
Win = False
listString = []

while True: ### code that initializes and plays the game
  print ("ROUND " + str(match))
  print ("")
  nonvalid = True
  while nonvalid: ### while loop for player 1's turn
    piece = input("Which piece would you like to move Player 1?: ")
    answer = input("Choose spot based on number board: ")
    if answer in "123456789" and piece in "123456789":
      print ("")
      match = match + 1
      turn = turn + 1
      gameboard(numPositions)
      print("")
      positions = moveValid(turn, answer, positions, piece)
      gameboard(positions)
      continued = winCon(turn, positions)
      break
    else:
      print ("Please choose a valid answer...")
  
  if continued == False and (turn == 2 or turn == 4 or turn == 6): ### checks if there is a win
    Win = False
    print ("The computer won!")
    break
  elif continued == False and (turn == 3 or turn == 5 or turn == 7):
    Win = True
    print ("Player 1 wins!")
    ai_learn(line, answer, Win, continued)
    break
  
  print ("ROUND " + str(match)) #what turn is it
  nonvalid = True
  while nonvalid: ### while loop for computer's turn
    print ("")
    match = match + 1
    turn = turn + 1
    gameboard(numPositions)
    print ("")
    positions = moveValid(turn, answer, positions, piece)
    gameboard(positions)
    continued = winCon(turn, positions)
    break

  if continued == False and (turn == 2 or turn == 4 or turn == 6): ### checks if there is a win
    Win = False 
    print ("The computer won!")
    break
  elif continued == False and (turn == 3 or turn == 5 or turn == 7):
    Win = True
    print ("Player 1 wins!")
    ai_learn(line, answer)
    break

 
  
  
  
  
  
  
  