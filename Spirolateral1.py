import turtle 
name = "main"
spirolateral = []
list_of_spirolaterals = []

def display_spiro():
    
    print (spirolateral)
    start()
	
def add_spiro():
  name_of_spirolateral = int(input("What will be the name of this spirolateral?"))
  list_of_spirolaterals.append(name_of_spirolateral)
  dig_root_num = int(input("Input a number from 2-9"))
  loop_num = 1 
  def digit_root(n): 
    return (n - 1) % 9 + 1 if n else 0 
	
  if name == "main": 
    while loop_num < 10:
      test = dig_root_num * loop_num
      spirolateral.append(digit_root(test)) 
      loop_num += 1  
  
  start()
  
def delete_spiro(): 
  print ("") 
  
def display(): 
  display_list = ["1 Display Spirolateral", "2 Add a Spirolateral", "3 Delete a Spirolateral", "4 Quit"] 
  for x in display_list: 
    print(x) 
  print("Input a number from 1-4") 
  
def menu():
    choice = int(input())
    while choice != 4:
        if choice == 1: 
            display_spiro() 
        if choice == 2: 
            add_spiro() 
        if choice == 3:
            delete_spiro
            
def start():
  display() 
  menu() 
  
start()
