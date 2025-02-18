

```md
# Snake, Water, Gun Game 🐍💧🔫

A simple Python-based **Snake, Water, Gun** game where you compete against the computer!  

## 📌 Rules
- **Snake (s) 🐍** beats **Water (w) 💧**  
- **Water (w) 💧** beats **Gun (g) 🔫**  
- **Gun (g) 🔫** beats **Snake (s) 🐍**  
- If both the player and the computer choose the same, it's a **Draw**.

## 🚀 How to Play
1. Run the Python script.
2. Enter your choice:  
   - `s` for Snake  
   - `w` for Water  
   - `g` for Gun  
3. The computer will randomly select its choice.
4. The winner is determined based on the rules above.

## 🛠 Installation
Ensure you have Python installed, then simply run:

```sh
python snake_water_gun.py
```

## 📝 Code Explanation
- The game randomly selects a choice for the computer.
- The user inputs their choice (`s`, `w`, or `g`).
- The game logic determines the winner based on predefined rules.
- The result is displayed.

## 🎯 Example Run
```
Enter Your Choice: s
You chose Snake
Computer chose Gun
You Lose
```

## 📌 Shortened Logic
The game also includes a **shorter winning logic**:
```python
if (computer - you) == -1 or (computer - you) == 2:
   print("You Lose")
else:
   print("You Win")
```



👨‍💻 Happy Coding!
```

