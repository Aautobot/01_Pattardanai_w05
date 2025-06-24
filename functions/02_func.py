# รับค่า Parameter
'''def func_name(parameter1, parameter2, ...):
    # คำสั่งที่ต้องการให้ทำ
    exe ; parameter1 + parameter2 = xxx'''
### ตัวอย่างการใช้งาน
'''def get_name(name):
    Function to greet a user with their name.
    print(f"Hello !!!, {name}")
name = input("Enter your name : ")
get_name(name)'''

# def add_number(a, b):
#     '''Function to add two numbers.'''
#     result = a + b
#     return result

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# sum = add_number(a, b)
# print(f"The sum of {a} and {b} is: {sum}")

def rectangle_area(length, width):
    '''Function to calculate the area of a rectangle.'''
    area = length * width
    frame = 2*(length + width)
    print(f"The area of the rectangle is: {area}")
    print(f"The frame of the rectangle is: {frame}")
    return area,frame

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area,frame = rectangle_area(length, width)
print(f"The area of the rectangle is: {area}")
print(f"The frame of the rectangle is: {frame}")