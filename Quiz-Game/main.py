# Quiz Game in Python - RealHaroon
 

questions=(
    "What programming language is used to create AI? : ",
    "Who is the Prime Minister of Pakistan? :",
    "What is the Richest Person on earth? :",
    "Which is the biggest animal? :",
    "What language is spoken in pakistan? :",

)
options=(("A. JS ","B. Java ","C. Python ","D. R "),
         ("A. Imran Khan ","B. Sehbaz Sharif ","C. Nawaz Sharif ","D. Bilawal Bhutto "),
         ("A. Jeff Bezoz ","B. Elon Musk ","C. Bill Gates ","D. Mark Zuckerberg "),
         ("A. Loin ","B. Zebra ","C. Rat ","D. Elephpant "),
         ("A. Urdu ","B. English ","C. Sindhi ","D. All of them "))

answers=("C","B","B","D","D")
guesses=[]
score=0
question_num=0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]}. Is the correct answer")
    question_num +=1

print("=================RESULTS==================")
print()
print("answers: ",end="")

for answer in answers:
    print(answer,end=" ")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int (score / len(questions) * 100)
print(f"Your Score is : {score}%")


