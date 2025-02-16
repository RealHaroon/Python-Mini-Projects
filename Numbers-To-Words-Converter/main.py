
# Names of Numbers
name = {
    1: " one", 2: " two", 3: " three", 4: " four", 5: " five",
    6: " six", 7: " seven", 8: " eight", 9: " nine", 10: " ten",
    11: " eleven", 12: " twelve", 13: " thirteen", 14: " fourteen",
    15: " fifteen", 16: " sixteen", 17: " seventeen", 18: " eighteen",
    19: " nineteen", 20: " twenty", 30: " thirty", 40: " forty",
    50: " fifty", 60: " sixty", 70: " seventy", 80: " eighty",
    90: " ninety", 100: " hundred"
}

num=int(input("Enter a Number: "))

if num <=100:
    if num in name:
        k=name.get(num)
        print(num," in words is ",k)
    else:
        b=num%10
        b=name.get(b)
        c=num//10
        c=c*10
        c=name.get(c)
        result=c+b
        print(num," in words is ",result)
else:
    print("Error! Enter a number from 1 to 100")