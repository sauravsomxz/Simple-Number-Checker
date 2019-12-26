# Author : Saurav Ranjan Maharana
# Date : 12th November, 2019
# Purpose : Learning Py!
# Contact : saurav.maharana07@gmail.com
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
if num1==num2==num3:
    print("All Three Numbers are equal.")
if num1==num2 or num1==num3 or num2==num3 or num3==num1:
    print("OK") 
else:
        print("None are equal.")