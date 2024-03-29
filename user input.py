# area of rectangle
# l = int(input("lenght of rec : "))
# b = int(input("breadth of rec : "))
# area = l*b
# print("area of rectangle is : ", area)

# area of circle
# r = float(input("radius of circle : "))
# area = 3.14*r*r
# print("area of circle : ", area)
# circum + 2*3.14*r
# print("circumference of circle is : " , circum)

# area of cube
# l = int(input("enter side of cube "))
# perimeter = 12*l
# volume = l**3
# area = 6*l**2
# print("area of cube is : ", area)
# print("perimeter of cube : ", perimeter)
# print("volume of cube is : ", volume)

# users age calculation

# birth_year = int(input("enter your birth year : "))
# current_year = int(input("enter current year : "))
# your_age = current_year - birth_year
# print("your age is : ", your_age)


#random input
r = int(input("enter any random betwen 1 - 10 : "))
s = int(input("enter one more random number betwen 1-10 : "))
t = input("select on operator which you wanna apply ( +, -, *, / ): ")
t=int(input("acc to you what should be the input : "))
g = 0
if(t=="+"):
   g = r+s
elif(t=="-"):
    g = r-s
    
elif(t=="*"):
   g =  r*s
elif(t=="/"):
    g =  r/s

print(g) 
if(t==g):
    print("correct answer ")
else:
    print("incorrect")