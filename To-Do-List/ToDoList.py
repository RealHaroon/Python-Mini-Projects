toDoLst=[]
taskHistory={}

def addTask(task): # Func1
    toDoLst.append(task)

def removeTask(task): # Func2
    toDoLst.remove(task)

def markDoneTask(task): # Func3
    taskHistory.update({task:"Done"})

def showAllTask(): #Func4
    count=0
    for i in toDoLst:
        count+=1
        print(count,i)
def showTaskHistory(): #FUnc 5
     return taskHistory

while(True):
    print("\t TO DO LIST")
    print("Press 1 to Add Task.")
    print("Press 2 to Remove Task.")
    print("Press 3 to Show All Task.")
    print("Press 4 to Marks Done Task.")
    print("Press 5 to Show Task History.")
    print("Press 6 to Exit.")

    inp=input("Enter Your Choice : ")

    if inp=="1":
        addTsk=input("Add Task : ")
        addTask(addTsk)
    if inp=="2":
        remTask=input("Remove Task : ").casefold()
        removeTask(remTask)
    if inp=="3":
        print("All Tasks : ")
        showAllTask()
    if inp=="4":
        mrkTask=input("Mark the done task: ")
        markDoneTask(mrkTask)
    if inp=="5":
        print("Task History : ")
        print(taskHistory)
    if inp=="6":
        print("Exited!")
        break
    
