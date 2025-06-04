Here’s a clean and well-formatted `README.md` for your **Expense Tracker by Haroon** project:

---

```markdown
# 💵 Expense Tracker CLI (By Haroon)

A simple command-line based **Expense Tracker** written in Python using **Pandas**.  
It allows you to add, view, filter, and summarize your personal expenses stored in a CSV file.

---

## 📦 Features

- ✅ Add new expenses (with date, category, amount, notes)
- 📄 View all expenses in a readable format
- 📅 Filter expenses between custom date ranges
- 🏷️ Filter by category (e.g., Food, Transport)
- 📊 View summary: total, average, and highest expense
- 💾 Automatically saves and loads from `expense.csv`

---

## 📁 File Structure

```

Expense-Tracker/
├── expense.csv          # Data file (auto-created if missing)
├── expense\_tracker.py   # Python script with ExpenseTracker class
└── README.md            # You're reading this!

````

---

## 🛠️ Requirements

- Python 3.x
- Pandas

Install pandas if you don't have it:

```bash
pip install pandas
````

---

## 🚀 How to Run

1. Make sure `expense.csv` exists in the `Expense-Tracker` folder
   (or let the script create it automatically).
2. Run the script:

```bash
python expense_tracker.py
```

---

## 🧠 Class Structure

### `ExpenseTracker`

| Method               | Description                                              |
| -------------------- | -------------------------------------------------------- |
| `addExpense()`       | Add a new expense with date, category, amount, and notes |
| `veiwExpenses()`     | View all expenses in table format                        |
| `filterByDate()`     | Show expenses between two dates                          |
| `filterByCategory()` | Show expenses for a specific category                    |
| `veiwSummary()`      | Display total, average, and highest expenses             |
| `main()`             | CLI loop to navigate the tracker                         |

---

## 📅 Example Usage

```
Expense Tracker By Haroon 💵 💻
1. Add Expense 
2. View All Expense 
3. Filter by Date 
4. Filter by Category 
5. View Summary 
6. Exit
Enter Your Choice (1-6):
```

---

## 🧑‍💻 Author

**Haroon** – BSCS Student, Passionate about Python & Projects.
University of Sindh, Laar Campus, Badin.

---

## 📌 Notes

* File path for CSV is set to `Expense-Tracker/expense.csv`
* Data is saved automatically after every new entry
* Date input can be left blank to use today’s date

---

## 📃 License

This project is open-source and free to use for educational or personal purposes.

---
** Created By Haroon (https://Github/RealHaroon)
```

---
