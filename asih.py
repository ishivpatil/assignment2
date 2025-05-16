#Takes an integer input from the user.
number =int(input("enter the number"))
if number %2 ==0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
# Uses a for loop to iterate over numbers from 1 to 50.
n='1 to 50'
for i in range(1,int(50)):
    print(i)

#Calculates the sum of all integers in this range
#range
list(range(1,50))
total=sum(range(1,50))
print(f"The sum of numbers from 1 to 50 is:{total}")
