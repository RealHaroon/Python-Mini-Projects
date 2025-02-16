#
def addTask():
    u_inp=input("Add Task : ")
    try:
     with open("To-Do-List\\task.txt","a")as f:
        f.write(u_inp +"\n")
        print("Task Added Succesfully")
    except:
       print("failed to add task")

def veiwTask():
   count=0
   try:
      with open("To-Do-List\\task.txt","r",encoding="utf-8") as f: #  UTF-8 encoding for emoji and check symbol 
         lines=f.readlines()
         for i in lines:
            count+=1
            print(count,".",i)
   except:
      print("Failed to veiw all task")

def doneTask():
  u_inp=input("Done Task: ")
  try:
   with open("To-Do-List\\task.txt", "r", encoding="utf-8") as f:  
    lines = f.readlines()  
   with open("To-Do-List\\task.txt", "w", encoding="utf-8") as f:  
    for line in lines:
        if u_inp in line:
            f.write(line.rstrip() + " ✔\n")  
            print("Marked!")
        else:
            f.write(line)
  except:
     print("Failed to Mark Task Done!")

def deleteTask():
   u_inp=input("Remove Task: ")
   try:
    with open("To-Do-List\\task.txt", "r") as f:
      lines=f.readlines()
    with open("To-Do-List\\task.txt", "w") as f:
      for line in lines:
         if u_inp not in line:
            f.write(line)  
      print("Task Has been removed")
   except:
      print("Failed to remove task!")

def clearTask():
   try:
      with open("To-Do-List\\task.txt", "w") as f:
         f.truncate()
         print("List Has been cleard!")
   except:
      print("Failed to clear task list!")

print(" 📜 To-Do-List By Haroon ")
while True:
   print("1. Add Task")
   print("2. Mark Task")
   print("3. View Task")
   print("4. Remove Task")
   print("5. Clear To Do List")
   print("6. Exit")

   u_inp=input("Enter Your Choice (1 - 6) = ")
   if u_inp == "1":
      addTask()
   elif u_inp == "2":
      doneTask()
   elif u_inp == "3":
      veiwTask()
   elif u_inp == "4":
      deleteTask()
   elif u_inp == "5":
      clearTask()
   elif u_inp == "6":
      break
   else:
      print("Invalid Input!")
