##1 reverse a list 

# list = [11,12,13,14,15]
# rev=[]
# for i in range(len(list)-1,-1,-1):
#     rev.append(list[i])
# print(rev)

##2 min and max of list
# list=[8, 2, 15, 3, 9]
# min=list[0]
# max=list[0]
# for i in range(0,len(list)):
#     if (min>list[i]):
#         min=list[i]
#     if (max<list[i]):
#         max=list[i]
# print("min and max of this list are : ", min," and ", max)

##3 # search element
# list=[5, 7, 3, 9]
# x=int(input("enter yout search value : "))
# for i in list:
#     if(x==i):
#         print("yes ",x," is present in this list at index ",list.index(x))
#         break
# else:
#     print("-1")
    
##4 remove diuplicate element
# list = [2, 5, 2, 8, 5,4,5,6,7,8,9,1,2,3,6,5,4,7,8,9,3,2,1,4,5,6,9,8,7, 1]
# for i in list:
#     for j in range(list.index(i)+1,len(list)):
#         if (i==list[j]):
#             list.remove(i)
# print(list)           

##5 sorting
# lis1=[3, 1, 5]
# lis2=[2, 4, 6]
# list=lis1+lis2
# for i in range(0,len(list)):
#     for j in range(0,len(list)):
#         if (list[i]<=list[j]):
#             list[i],list[j]=list[j],list[i]
# print(list) 

##6 






##7
# list=[1,2,3,4,5,6,7,8,9]
# y=int(input("size sub list you want : "))
# x=[]
# for i in range(0,len(list),y):
#     x.append(list[i:i+y])
# print(x)


#8 #sum of all element in a list
# list=[5, 10, 2, 8, 1]
# sum=0
# for i in list:
#     sum+=i
# print(sum)



##9 rotation of element
# list=[1, 2, 3, 4, 5]
# rotate=int(input("enter rotation : "))
# for i in range(0,rotate):
#     a=list.pop(len(list)-1)
#     list.insert(0,a)
# print(list)

##1 : Create a list with the names of your favorite fruits. Print the list. 
# list=["apple", "mango", "banana", "grapes"]
# print(list)

##2 : Given a list of numbers, double each element and print the modified list.

# list = [1,2,3,4,5,6,7,8,9]
# mdlist=[]
# for i in list:
#     i*=2
#     mdlist.append(i)
# print(mdlist)

##3 :  Create a list of cities. Print the first and last elements using indexing.
# cities=["gwalior", "indore", "bhopal", "ujjain", "mumbai"]
# print("first element of your list is : ",cities[0],"\n" "and last element of your list is : ",cities[len(cities)-1])

##4 : Generate a list of squares for numbers 1 to 10 using list comprehension. Print the resulting list.
# list=[]
# for i in range(1,11):
#     i=i**2
#     list.append(i)
# print(list)

##5 : Take a list of words and sort them in alphabetical order. Print the sorted list.
list=["oigi","kokf","iofv","kfrek","aoskd"]
a=len(list)
for i in range(0,a):
    for j in range(0,a-i,-1):
        if(list[i]>list[j]):
            list[i],list[j]=list[j],list[i]
print(list)


##6 : Given a list of ages, filter out the adults (age >= 18). Print the modified list
# age=[12,11,18,19,15,22,33,66,55,44,75,85,69,58,42,43,31]
# adult_list=[]
# for i in age:
#     if(i>=18):
#         adult_list.append(i)
# print(adult_list)

##7 : Create two lists of colors and concatenate them. Print the combined list.
# lis1=["blue","pink","red"]
# lis2=["orange","black", "white"]
# list=lis1+lis2
# print(list)

##8 : Given a list of animals, remove a specific animal from the list. Print the modified list.
# list=["dear","bear","lion", "bufflo", "cow", "dog","cat"]
# x=input("enter the animal's name which you wanna remove : ")
# for i in list:
#     if(i==x):
#         list.remove(i)
# print(list)

##9 : Write a function that takes a list of numbers as input and returns the sum of the squares of each number.
# list=[22,33,44,55,66,99,88,77,11]
# lis=[]
# for i in list:
#     i=i**2
#     lis.append(i)
# print(lis)

##10 : Reverse the order of elements in a given list of characters. Print the reversed list.
# list=["a","b","c","d","e","f","g","h","i"]
# lis=[]
# for i in range(len(list)-1,-1,-1):
#     lis.append(list[i])
# print(lis)

