import math

'''
age = 30
height = 1.7
complex_num = 4 + 1j

b = int(input("Enter the base number of the triangle: "))
h = int(input("Enter the height number of the triangle: "))
area = (0.5 * b * h )

print("The area of the triangle is:", area)


sides_a = int(input("Enter the number of side A of the triangle: "))
sides_b = int(input("Enter the number of side B of the triangle: "))
sides_c = int(input("Enter the number of side C of the triangle: "))
perimeter = (sides_a + sides_b + sides_c)

print("The perimeter of the triangle is:", perimeter)

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

area_of_rect = length * width
peri = 2 * (length + width)
print("The area of the rectangle is: ", area_of_rect)
print("The perimeter of the rectangle is: ",peri)


pi = 3.14
radius = int(input("Enter the radius:- "))
area_of_circle = pi * radius * radius
c = 2 * pi * radius

slope = 2
y_intercept = -2
x_intercept = 2/2

print(f"slope: ",slope)
print(f"x_intercept: ({x_intercept, 0})")
print(f"y_intercept: ({0,y_intercept})")


x1, y1 = 2, 2
x2, y2 = 6, 10
slope2 = (y2 - y1)/(x2 - x1)
euclidean_d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

if slope == slope2:
    print("the slope is thesame")
else
    print("the slopes are different")
'''

x = -3
y = (x**2 + 6*x + 9)
print("the value of y is: ", y)

str1, str2 = 'python', 'dragon'
len_str1 = len(str1)
len_str2 = len(str2)

if len_str1 != len_str2:
    print("strings are not of equal length")
else:
    print("strings are equal")
    print("The concatenation of the strings is: ", str1 + ' ' + str2)

on_comparison = ('on' in str1) and ('on' in str2)

if on_comparison == True:
    print("Both strings contain the word 'on'")
else:
    print("Both strings do not contain the word 'on'")

sentence = 'i Hope this course is not full of jargon'
check = ('jargon' in sentence)
if check == True:
    print("The word 'jargon' is present in the given string")

text = 'python'
tl = len(text)
fl = float(tl)
st = str(fl)

print("The length of the string is: ", tl)

print("The float equivalent of the length is: ", fl)

print("The string equivalent of the float length is: ", st)


number = int(input("Enter number to check even: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


floor_division = 7//3
converted_value = int(2.7)

if floor_division == converted_value:
    print("The floor division is equal to the converted value")

hour = int(input("Enter Hours: "))
rate = int(input("Enter Rate per hour: "))
pay = hour * rate

print("The pay is: ", pay)

seconds_lived = 365 * 24 * 60 * 60
years_lived = int(input("Enter number of years lived: "))
print(f'You lived for: {years_lived * seconds_lived} seconds')


print('n  n^1  n^2  n^3  n^4')
for n in range(1,6):
    print(f'{n}    {n**1}    {n**2}    {n**3}    {n**4}')

    








