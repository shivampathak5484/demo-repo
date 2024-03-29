'''q4. Write a Python program to reverse a given string'''
# x=input("enter your string : ")
# print(x[::-1])

'''5. Given a list of numbers, write a Python program to calculate the average of all the
 numbers.'''
# x=[1,2,3,4,5,6,7,8,9]
# print(sum(x)/len(x))

''' 6. Explain the di erence between '==', 'is', and 'in' operators in Python with examples.
'''

''' 7. Write a Python program to calculate the factorial of a given number.
'''
# x=int(input(" enter number : "))
# fact=1
# for i in range(2,x+1):
#     fact*=i
# print(f"factorial of {x} is : {fact}")

''' 8. Write a Python program to count the occurrences of each word in a given string.
'''
# x=input("enter your string : ")
# list=x.split(" ")
# dict={}
# for i in list:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict) 

''' 9. Given two lists, write a Python program to concatenate them into a single list.
'''
x=[1,2,3,4,5]
y=[6,7,8,9,0]
print(x+y)