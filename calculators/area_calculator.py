print("Welcome to the Area Calculator.\nPlease select a shape from the menu below:")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")

def area_of_square(length):
    return length * length

def area_of_rectangle(length, width):
    return length * width


user_option = int(input("Please enter your choice: "))
if user_option == 1:
    length = float(input("Enter the length of the square: "))
    print(area_of_square(length))
elif user_option == 2:
    length = float(input("Enter the length of rectangle: "))
    width = float(input("Enter the width of rectangle: "))
    print(area_of_rectangle(length, width))
elif user_option==3:
    base_of_triangle=float(input("Enter the base of triangle: "))
    height_of_triangle=float(input("Enter the height of triangle: "))
    area1=base_of_triangle*height_of_triangle
    print(area1/2)
elif user_option==4:
    radius_of_circle=float(input("Enter the radius of the circle: "))
    print(3.141592653589793238462643383279502884197*radius_of_circle*radius_of_circle)
else:
    print("Invalid Input")              
