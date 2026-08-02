## Task 3 M.I.A Robotics 
This project is a **To-do-List** for Lightning McQueen,where it allows McQueen to control tasks with an ordered menu of options :
1. Add a task
2. View my to-do list
3. Mark a task as done ✅
4. Remove a task
5. Quit ❌

This project has some *outstanding* features which include:
* Saving this list permenantly so that it's still
there the next time McQueen opens
*Confirming each move was successfully done

In order to run this file,you need just:
 * Visual studio code with Code Runner ***Extension***
 * Take care to follow the exact instructions asked
    * For example :
          *When asked ***Enter task with its order number*** so enter **for example**:1-Get new tires from Luigi

#### **CHALLENGE** that faced me
<mark>Trying to add the bonus task which states:
> If your program saves the to-do list to a file so it's still
there the next time McQueen opens it you'll get bonus
points.
***How I solved it:***
* First I watched youtube video explaining [Reading and Writing with External Text Files](https://youtu.be/JgllElxpSj0?si=FGCvltCb0F4XnYvx)
* I searched for file handling concepts(specifically for the syntax in python for file handling ) ,**for example:**
  ```
  with open("textfile.txt","w",encoding="utf-8") as file:
   file.writelines(list)
  ```
The real challenge was when marking the task as done (move 3 ) but I managed to read all the text file into a list then specifying the line to modify in list  with list index then overwriting the whole text file with the modified list 
