# list=[]
# for i in range(45,67):
#     if(i%2==0):
#         list.append(i)
# print(list)

#reverse list
# list=[1,2,3,4,5,6,7,8,9,10,11,22,33]
# print(len(list))
# rev=[]
# for i in range(len(list)-1,-1,-1):
#     rev.append(list[i])
# print(rev)

#sub list

# list=[11,22,33,44,55,66,77,88,99,10,1,2,3,4,5,6,7,8,9]
# sub=[]
# for i in list:
#     check=True
#     for j in range(2,i):
#         if(i%j==0):
#             check=False
#     if(check==True):
#             sub.append(i)
# print(sub)

#min // max
# list=[22,55,33,55,4,4,44,5,45,5,3,3,5,2,0,5,2,10]
# for i in list:
#     for j in list:
#         if(i>j):
#             i=j
#     break   
# for k in list:
#     for l in list:
#         if(k<l):
#             k=l
#     break   
# print("min of this list is", i)
# print("max of this list is", k)

##chek exitance
# a = int(input("enter your number : "))
# list = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]
# for i in list:
#     if(a==i):
#         print("your number is present at", list.index(i), "position")
 


# sorting in ascending
# list = [6,4,3,2,3,4,5,6]
# for i in range(0,len(list)):
#     for j in range(i+1,len(list)):
#         if(list[i]>list[j]):
#             list[i],list[j]=list[j],list[i]
# print(list)
# sorting in decending
# list = [6,4,3,2,3,4,5,6]
# for i in range(0,len(list)):
#     for j in range(i+1,len(list)):
#         if(list[i]<list[j]):
#             list[i],list[j]=list[j],list[i]
# print(list)

# unique element
# list = [6,4,3,2,3,4,5,6]
# for i in range(0,len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]==list[j]:
#             list.remove(list[i])
# print(list)

