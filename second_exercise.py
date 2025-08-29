'''
Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
'''

import math
radius = float(input("Enter the radius: "))
area = math.pi *(radius **2)
print(f"Circle area is: {area} ")

'''
Write a program that asks the user for the length and width of a rectangle. 
The program then prints out the perimeter and area of the rectangle. 
The perimeter of a rectangle is the sum of the lengths of each four sides.
'''

length = float(input("Enter length of a rectangle: "))
width = float(input("Enter width of a rectangle: "))
perimeter = 2* (length + width)
print(f"perimeter of a rectangle is {perimeter}")

'''
Write a program that asks the user for three integer numbers. 
The program prints out the sum, product, and average of the numbers.
'''

num1 = float(input("Enter random number: "))
num2 = float(input("Enter random number: "))
num3 = float(input("Enter random number: "))
sum = num1 + num2 + num3
product = num1 * num2 * num3
average  = sum/3
print(f"Sum of your number {sum}")
print(f"product of your number {product}")
print(f"average of your number {average}")

'''
Write a program that asks the user to enter a mass in medieval units: 
talents (leiviskä), pounds (naula), and lots (luoti). 
The program converts the input to full kilograms and grams and outputs the result to the user:

One talent is 20 pounds.
One pound is 32 lots.
One lot is 13,3 grams.
'''