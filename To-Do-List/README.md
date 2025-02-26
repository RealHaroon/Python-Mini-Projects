# 📝 To-Do List by Haroon

A simple **command-line To-Do List** application in Python that allows users to **add, view, mark, delete, and clear tasks**. The tasks are stored in a text file (`task.txt`) for persistence.

## 🚀 Features
- 📌 **Add Tasks**: Add new tasks to the list.
- ✅ **Mark Tasks as Done**: Mark completed tasks with a ✔ symbol.
- 📖 **View Tasks**: Display all tasks with numbering.
- ❌ **Remove Tasks**: Delete specific tasks from the list.
- 🗑️ **Clear All Tasks**: Remove all tasks at once.
- 🔄 **Persistent Storage**: Tasks are saved in `task.txt`.

## 📂 Project Structure
```
To-Do-List/
│── task.txt          # Stores all tasks
│── todo.py           # Main script
│── README.md         # Documentation
```

## 🛠️ How to Run
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/To-Do-List.git
cd To-Do-List
```

### **2️⃣ Run the Script**
```bash
python todo.py
```

## 📌 Usage Guide
When you run the script, you will see the following menu:
```
 📜 To-Do-List By Haroon 
1. Add Task
2. Mark Task
3. View Task
4. Remove Task
5. Clear To Do List
6. Exit
```

### **1️⃣ Add a Task**
Select **option 1**, then enter a task:
```
Enter Your Choice (1 - 6) = 1
Add Task: Buy groceries
Task Added Successfully
```

### **2️⃣ View All Tasks**
Select **option 3** to view your tasks:
```
1. Buy groceries
```

### **3️⃣ Mark a Task as Done**
Select **option 2**, then enter the task name:
```
Done Task: Buy groceries
Marked!
```
Now, the task appears as:
```
1. Buy groceries ✔
```

### **4️⃣ Remove a Task**
Select **option 4** and enter the task name:
```
Remove Task: Buy groceries
Task Has been removed
```

### **5️⃣ Clear All Tasks**
Select **option 5** to delete all tasks.
```
List Has been cleared!
```

### **6️⃣ Exit the Program**
Select **option 6** to exit.

## 🛠️ Requirements
- Python 3.x

## 🏆 Future Improvements
- 🖥️ Add a **GUI version** (Tkinter or PyQt)
- 🕰️ Add **due dates & reminders**
- 📊 Add **task categories & priorities**

## 📜 License
This project is open-source and free to use!

---
Made with ❤️ by **Haroon** 🚀