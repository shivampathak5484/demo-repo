##q1 : Find the union and intersection of two sets.
# x={1,2,3}
# y={2,3,4,5}
# intersection=set()
# ## z=x.union(y)
# ## v=x.intersection(y)
# for i in list(x):
#     for j in list(y):
#         if(i==j):
#             intersection.add(i)
# print(intersection)

##q2 : Remove all elements from a set that are present in another set.
# set1={1,2,3,4}
# set2={3,4,5,6}
# # v=set1.difference(set2)
# for i in list(set1):
#     for j in list(set2):
#         if(i==j):
#             set1.remove(i)
# print(set1)

##q3 : Check if two sets are disjoint (no elements in common).
# set1={1,2,3,4}
# set2={5,6,7,8}
# # # if(set1.intersection(set2)==):
# # #     print("set1 and set2 are disjoint")
# # # else:
# # #     print("sets are joint to each other")
# check = True
# for i in set1:
#     if i in set2:
#         check =False
# if check == True:
#     print("sets are disjoint")
# else:
#     print("sets are joint")

##q4 : Generate a set of unique numbers from a list with duplicates.
# list=[1,2,3,4,2,3,4,1]
# # x=set(list)
# # print(x)
# set()
# for i in list:
#     set.add(i)
# print(set)


##q5 : Write a program to find the symmetric difference of two sets.
# x={1,2,3,4}
# y={3,4,5,6,7,8}
# # x=set1.difference(set2)
# # print(x)
# difference = set()
# for i in list(x):
#     check=True
#     for j in list(y):
#         if i==j:
#             check=False
#     if check==True:
#         difference.add(i)       
# print(difference)

##q6 : Count the number of elements in a set.
# set={1,2,3,4,5,6}
# count=0
# for i in list(set):
#     count+=1
# print(count)

##q7 : Check if a specific element is present in a set.
# x={1,2,3,4,5,6}
# y=int(input("enter your element : "))
# check=True
# for i in list(x):
#     if i==y:
#         print("yes your element is present in this set ")
#         check=False
#         break
# if check==True:
#     print("your element is not present in this set")

##q8 : Remove all elements smaller than a given value from a set.
# x={1,2,3,4,5,6}
# y=int(input("enter your value : "))
# for i in list(x):
#     if i<=y:
#         x.remove(i)
# print(x)

##q9 : Find the subset of one set that is present in another set.
# x={1,2,3,4,5,6}
# y={4,5,6,7,8,9}
# subset=set()
# for i in list(x):
#     for j in list(y):
#         if i==j:
#             subset.add(i)
# print(subset)

##q10 : Implement a basic dictionary using sets and functions (key-value pairs and lookups).
