def options():
    print (f"Menu of options to modify your to do list:")
    print ("1-Add a task")
    print ("2-View my to-do list")
    print ("3-Mark a task as done")
    print ("4-Remove a task")
    print ("5-Quit")   
def List():
 print ("Your list up till now :")
 with open ("tasks.txt","r") as file:
    tasks = file.read()
    print (tasks)
print (f"WELCOME CHAMP MCQUEEN!")
print (f"Gotta get ready for a huge upcoming adventure ahead!")
move=0
while move!=5 :
 options()
 move=int (input ("What is the move on your head champ?"))
 if move==1 :
    user_ip=input("Enter the task you want to add with its order number:")
    with open("tasks.txt","a") as file :
       file.write(user_ip +"-->pending"+"\n") 
       
    print ("Your task has been successfully added to your TO-DO-LIST") 
 if move==2:
    List()
 if move==3:
    order=int(input("What is the order number of the task completed?"))
    userInput=input("Enter the task completed with its order number:")
    with open("tasks.txt","r",encoding="utf-8") as file:
       lines= file.readlines()
    lines[order-1] = userInput + "-->completed"
    with open("tasks.txt", "w", encoding="utf-8") as file:
       file.writelines(lines)
    print ("This task has been successfully checked off from your TO-DO-LIST") 
 if move==4:
    order=int(input("What is the order number of the task to be removed?"))
    userInput=input("Enter the task to be removed with its order number:")
    with open("tasks.txt","r",encoding="utf-8") as file:
        lines= file.readlines()
    lines[order-1] = ""
    with open("tasks.txt", "w", encoding="utf-8") as file:
       file.writelines(lines)
       
    print ("This task has been successfully removed from your TO-DO-LIST") 

print("It has been a great run champ!\nSee you Later!")