spirolateral = []
list_of_spirolaterals = []

def display_spiro():
  print("List of Spirolaterals to choose from: ")
  for i in range(len(spirolateral)):
    print (spirolateral[i][0])

  check_spiro = str(input("What spirolateral do you want to display? "))
  for i in range(len(spirolateral)):
    if check_spiro == spirolateral[i][0]:
      print (spirolateral[i])
      break
    
def digit_root(n): 
    return (n - 1) % 9 + 1 if n else 0
  
def add_spiro():
  temp_entry_spirolateral = []
  name_of_spirolateral = str(input("What will be the name of this spirolateral? "))
  for i in range(len(spirolateral)):
    if name_of_spirolateral == spirolateral[i][0]:
      print (name_of_spirolateral, "already exists")
      break
  while True:
    dig_root_num = input("Input a number from 2-9: ")
    try:
      dig_root_num = int(dig_root_num)
      break
    except:
      print("Please enter an integer")

  temp_entry_spirolateral.append(name_of_spirolateral)
  loop_num = 1
  while loop_num < 10:
    test = dig_root_num * loop_num
    temp_entry_spirolateral.append(digit_root(test))
    loop_num += 1

  spirolateral.append(temp_entry_spirolateral)

def delete_spiro():  
  del_spiro=str(input("Which spirolateral do you want to delete? "))
  for i in range(len(spirolateral)):
    if del_spiro == spirolateral[i][0]:
      spirolateral.pop(i)
      break

#Shows the user the options and lets them input what option they want to do.
def display():
  global choice
  display_list = ["1 Display Spirolateral", "2 Add a Spirolateral", "3 Delete a Spirolateral", "4 Quit"] 
  for x in display_list: 
    print(x)
  choice = input("Input a number from 1-4: ")
  #Prevents a error by the user inputting letters
  try:
    choice = int(choice)
  except:
    print("Please enter an integer")
  
def menu():
      while choice != 4:
          if choice == 1: 
              display_spiro() #Calls for the display_spiro to run (above)
          if choice == 2:
              add_spiro() 
          if choice == 3:
              delete_spiro()
          display()
            
def start():
  display() 
  menu() 
  
start()
