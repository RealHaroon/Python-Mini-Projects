# Names of Numbers
name = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
    50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
    90: "ninety"
}

def number_to_words(num):
    if num == 10000:
        return "ten thousand"
    
    words = ""
    
    if num >= 1000:
        words += name[num // 1000] + " thousand"
        num %= 1000
    
    if num >= 100:
        words += " " + name[num // 100] + " hundred"
        num %= 100
    
    if num > 0:
        if words:
            words += " and"
        if num in name:
            words += " " + name[num]
        else:
            words += " " + name[num // 10 * 10] + " " + name[num % 10]
    
    return words.strip()
    
num = int(input("Enter a Number (1-10000): "))

if 1 <= num <= 10000:
    print(num, "in words is", number_to_words(num))
else:
    print("Error! Enter a number from 1 to 10000")
