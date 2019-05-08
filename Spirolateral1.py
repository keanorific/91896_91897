spirolateral = []
list_of_spirolaterals = []

def display_spiro():
    ds = str(input("What spirolateral do you want to display?"))
    if ds in list_of_spirolaterals:
        print (list_of_spirolaterals[ds])

def digit_root(n): 
  return (n - 1) % 9 + 1 if n else 0


   
def add_spiro():
  name_of_spirolateral = str(input("What will be the name of this spirolateral?"))
  list_of_spirolaterals.append(name_of_spirolateral)
  dig_root_num = int(input("Input a number from 2-9"))
  loop_num = 1
  while loop_num < 10:
    test = dig_root_num * loop_num
    spirolateral.append(digit_root(test))
    print(digit_root(test))
    loop_num += 1  

def delete_spiro(): 
  del_spiro = str(input("Which spirolateral do you want to delete?"))
  if del_spiro in list_of_spirolaterals:
      list_of_spirolaterals.remove(del_spiro)
      print(del_spiro, "has been deleted")
  else:
      print("There is no spirolateral called", del_spiro)
  
def display():
  global choice
  display_list = ["1 Display Spirolateral", "2 Add a Spirolateral", "3 Delete a Spirolateral", "4 Quit"] 
  for x in display_list: 
    print(x) 
  print("Input a number from 1-4")
  choice = int(input())
  
def menu():
    while choice != 4:
        if choice == 1: 
            display_spiro()
            display()
        if choice == 2:
            add_spiro()
            display()
        if choice == 3:
            delete_spiro()
            display()
            
def start():
  display() 
  menu() 
  
start()
