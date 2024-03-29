''' q11. Write a Python function to check if a given string is a palindrome or not.'''
# def palindrome(s1):
#     if s1 == s1[::-1]:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")
# s1 = input("Enter the string: ")
# palindrome(s1)


'''q12 :  Given a list of integers, write a Python program to find the sum of all even numbers
 in the list.'''
# a=[1,2,3,4,5,6,7,8,9]
# sum=0
# for i in a:
#     if i%2==0:
#         sum+=i
# print(sum)

'''q13. Explain the purpose of list comprehension in Python with an example.'''
'''List comprehension is like a shortcut way in Python to make lists. Instead of writing long loops to create lists, you can use list
comprehension to do it more quickly and with fewer lines of code.
For example:
If we want to make a list of numbers squared from 0 to 9,here is the code[x**2 for x in range(10)]'''


'''q14. Write a Python class named 'Employee' with attributes name, age, and salary.
 Implement a method to display the employee details. Create an instance and call the
 method.'''
# class Employee:
#     def __init__(self,name,age,salary):
#         self.name=name 
#         self.age=age
#         self.salary=salary

#     name=""
#     age=0
#     salary=0.0

#     def display_details(self):
#         print(f"name of your employee is : {self.name}")
#         print(f"age : {self.age}")
#         print(f"salary : {self.salary}")

# a=Employee("shivam",21,50000)
# a.display_details()

''' q15. Write a Python program to find the factorial of a given number.
'''
# x=int(input(" enter number : "))
# fact=1
# for i in range(2,x+1):
#     fact*=i
# print(f"factorial of {x} is : {fact}")

''' q16. Write a Python program to remove duplicates from a list while preserving the order
 of elements'''
# list=[1,2,3,4,5,6,7,8,9,2,1,3,4,5,6,7,8,9,4,5,6,9,8,7,1,2,3]
# lis1=[]
# for i in list:
#     if i not in lis1:
#         lis1.append(i)
# print(lis1)   

''' q17. Explain the di erence between 'append()' and 'extend()' methods in Python lists with
 examples.'''
'''
append() adds a single element to the end of the list,
but extend() adds multiple elements to the end of the list by appending each element from an iterable.

append() takes a single argument (the element to be added), while extend() takes an iterable as its argument.

'''
    
''' q18. Given a list of strings, write a Python program to count the occurrences of each
 word in the list.'''
# list=["shivam","sumit","sharda","santosh","deepak","manvendra","sumit","shivam","sharda","santosh"]
# dict={}
# for i in list:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict) 

''' q19. Write a Python program to find the second largest element in a list'''
# list=[5,3,2,6,4,1,8,9,7]
# list.sort()
# print(list[-2])

''' q20. Write a Python program to generate a Fibonacci sequence up to a specified number
 of terms.'''
# num_terms = int(input("Enter your number : "))
# fib = []  
# a, b = 0, 1
# for _ in range(num_terms):
#     fib.append(a)  
#     a, b = b, a + b  
# print(fib)

''' q21. Given a dictionary, write a Python program to find and print the keys with the
 highest value'''
x={1:2,2:3,3:8,4:6,5:4} 
max_value = max(x.values())
highest_value_keys = []
for key, value in x.items():
    if value == max_value:
        print(key)


