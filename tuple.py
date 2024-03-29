##1 : Given a tuple of fruits, find the ones with more than 5 characters.
# tuple=("apple","mango","grapes", "orange", "kiwi")
# list=[]
# for i in tuple:
#     if(len(i)>5):
#         list.append(i)
# print(list," these fruits are more tan 5 character ")

##2 : Count the number of times a specific tuple element appears in another tuple.
# tup=(1,2,1,2,3,4,5,6,2,3,4,5,3,4,5,6)
# count=0
# x=int(input("choose specific element from  tup1 (1,2,3,4,5,6) : "))
# for i in tup:
#     if(i==x):
#         count+=1
# print("your element is ", count," times present in this tuple")

##3 : Check if a given tuple is a prefix of another tuple.
# t1=(1,2,3)
# t2=(1,2,3,7,8,9)
# is_prifix=True
# for i in range(len(t1)):
#     if t1[i]!=t2[i]:
#         is_prifix=False
#         break
# print(is_prifix)


##4 : Extract a specified element from a tuple based on its position.
# t1=(1,2,3,4,5,6,7,8,9)
# x=int(input("enter your specified element : "))
# print(t1[x])


##5 : Extract a specified element from a tuple based on its position.
# tup1=(1,2,3,4)
# tup2=(5,6,7,8)
# tup=tup1+tup2
# print(tup)

##6 : Sort a tuple based on a specific element in each tuple.
# t1=(6,3,5,4,2,1,8,9,7)
# for i in range(0,len(t1)):
#     for j in range(i+1,len(t1)):
#         if t1[i]>=t1[j]:
#             t1[i],t1[j]=t1[j],t1[i]
# # print(t1)

###########7 : Check if all elements in a tuple are of the same data type.
tuple=(1,2,3,"orange")
for i in range(0,len(tuple)):
    while(i<len(tuple)):
        if(type(tuple[i])!=type(tuple[i+1])):
            print("all element of this tuple are not of same data type")
else:
    print("all elements are of same data type")

##8 : Find the average of all numerical elements in a tuple.
# tup=(1,2,3,"apple","orange", 4,5,6,7,8,9)
# count=0
# sum=0
# for i in tup:
#     if(type(i)==int):
#         sum+=i
#         count+=1
# print("avg of numerical values are : ",sum/count)

##9 : Convert a tuple into a list and vice versa.
# tup=(1,2,3)
# list=list(tup)
# print(list,type(list))
# t=tuple(list)
# print(t,type(t))

##10 : Create a function that returns the first and last element of a tuple as a new tuple.
# tup=(1,2,3)
# print("first and last elememt of your tuple are : ", tup[0]," and ",tup[len(tup)-1])

