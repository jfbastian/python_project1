"""
print('Hello')
#input() function takes all inputs as a string only!! | stored as a string
age = input("Enter your age:\n ") #'\n' for new line
name = input("Enter your name: ")
#type() check the type of input enter
print("Type of number:", type(age))
print("Type of number:", type(name))

#int() convert input to integer
num = int(input("Enter a number: "))
print(num, " ", type(num))

floatNum = float(input("Enter a decimal number: "))
print(floatNum, " ", type(floatNum))


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
addition = num1 + num2
#{} - .format()
print("The sum of the two given numbers is {}".format(addition))


#taking user inputs as strings and splitting on each character
#using list() to convert into list of characters
list1 = list(input("Enter elements of list1: "))
list2 = list(input("Enter elements of list2: "))
#appending list2 into list1 using .append function
for i in list2:
    list1.append(i)
print(list1)    

#conditional output in python
#if-else and elif(else if) statement
a = 3
b = 9
if b % a == 0 :
    print("b is divisible by a")
elif b + 1 == 10 :
    print("Increment in b produces 10")
else:
    print("You are in else statement")

"""
#functions in python 
#notice the indentation
def checkDivisibility(a, b):
    if a % b == 0 :
        print("a is divisible by b")
    else:
        print("a is not divisible by b")  
#Driver program to test the above function
checkDivisibility(4,2)



