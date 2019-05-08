#Starting lists that will be added to as the user adds more spirolaterals
spirolateral = []
#Displays the spirolaterals by asking the user which spirolateral they want to display then checking if that spirolateral exists in the array
def display_spiro():
  print("List of Spirolaterals to choose from: ")
  for i in range(len(spirolateral)):
    print (spirolateral[i][0])

  checkSpiro = str(input("What spirolateral do you want to display? "))
  for i in range(len(spirolateral)):
    if checkSpiro == spirolateral[i][0]:
      print (spirolateral[i])
      break
#Codes for the digital root, adding the digits together for numbers having double or more digits
def digit_root(n): 
    return (n - 1) % 9 + 1 if n else 0
#Adds a spirolateral and adds it to the list to be displayed or deleted
def add_spiro():
  spirolateralListEntry = []
  spirolateralName = str(input("What will be the name of this spirolateral? "))
  for i in range(len(spirolateral)):
    if spirolateralName == spirolateral[i][0]:
      print (spirolateralName, "already exists")
      break
  while True:
    digitalRootNum = input("Input an integer: ")
    try:
      digitalRootNum = int(digitalRootNum)
      break
    except:
      print("Please enter a integer")
            
  spirolateralListEntry.append(spirolateralName)
  loopNum = 1
  while True:
    spirolateralListElement = digitalRootNum * loopNum
    if digit_root(spirolateralListElement) in spirolateralListEntry:
      break
    spirolateralListEntry.append(digit_root(spirolateralListElement))
    loopNum += 1

  spirolateral.append(spirolateralListEntry)

def delete_spiro():  
  deleteSpiro=str(input("Which spirolateral do you want to delete? "))
  for i in range(len(spirolateral)):
    if deleteSpiro == spirolateral[i][0]:
      spirolateral.pop(i)
      break

#Shows the user the options and lets them input what option they want to do.
def display():
  global choice
  displayList = ["1 Display Spirolateral", "2 Add a Spirolateral", "3 Delete a Spirolateral", "4 Quit"] 
  for x in displayList: 
    print(x)
  choice = input("Input a number from 1-4: ")
  #Prevents a error by the user inputting letters and instead just asks the user again
  try:
    choice = int(choice)
  except:
    print("Please enter an integer: ")
  
def menu():
      while choice != 4: #If the input is 4, the program will quit
          if choice == 1: 
              display_spiro() #Calls for the display_spiro to run (above)
          if choice == 2:
              add_spiro() 
          if choice == 3:
              delete_spiro()
          display() #If the user inputs letter or numbers ouside of 1-4, the program will ask the user again
      print("Goodbye!")
            

display() 
menu() 
  

