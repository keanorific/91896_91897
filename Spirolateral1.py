import turtle 
name = "main"
spirolateral = []


def display_spiro():
    print (spirolateral)
    start()
	
def add_spiro():
  
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
  upper_lim = 5
  lower_lim = 0
  choice = int(input())
  if choice > lower_lim or choice < upper_lim:
    if choice == 1: 
      display_spiro() 
    if choice == 2: 
      add_spiro() 
    if choice == 3:
      delete_spiro 
    if choice == 4: 
      exit
  else:
    print("That wasn't valid input")
    start()
	
def start():
  display() 
  menu() 
  
start()

