##q1 : Given a dictionary of student names and grades, find the student with the highest grade.
# student={"shivam":98,"sumit":95,"deepak":94,"amit":99}
# highest_grade=0
# for i in student.items():
#     if(i[1]>highest_grade):
#         highest_grade=i[1]
# print("highest_grade : ",highest_grade)

##q2 : Count the occurrences of each letter in a given word using a dictionary.
# word=input("enter your word : ")
# count={}
# for letter in word:
#     if letter in count:
#         count[letter]+=1
#     else:
#         count[letter]=1
# print(count)

##q3 : Print all key-value pairs in a dictionary sorted by key.
# dict={"shivam":98,"sumit":97,"amit":96,"deepak":95}
# new_dict={}
# key=[]
# for i in dict.keys():
#     key.append(i)
# for j in range(0,len(key)):
#     for k in range(j+1,len(key)):
#         if key[j]>key[k]:
#             key[j],key[k]=key[k],key[j]
# # print(key)
# # for i in key:
# #     print(i, ":" , dict[i], end=" , ")
# for i in key:
#     new_dict[i]=dict[i]
# print(new_dict)

##q4 : Update a specific value associated with a key in a dictionary.
# dict={"name":"shivam","age":21,"city":"gwalior"}
# print(dict)
# # dict.update({"name":"sumit"})
# dict["name"]="sumit"
# print(dict)

##q5 : Merge two dictionaries into one, with duplicate keys handled appropriately.
# dict1={"mango":5,"apple":6,"banana":7}
# dict2={"mango":8,"oranges":9,"guava":4}
# merge_dict=dict1.copy()
# merge_dict.update(dict2)
# print(merge_dict)


##q6 : Check if a specific key exists in a dictionary.
# dict={"name":"shivam","age":21,"city":"indore","college":"m.i.t.s."}
# check=input("enter your specific key for search : ")
# for i in dict.keys():
#     if i==check:
#         print("yes your key is present in this dict ")
#         break
# else:
#     print("not present!")

##q7 : Delete a key-value pair from a dictionary based on the key.
# dict={"name":"shivam","city":"gwalior","state":"madhya pradesh","occupation":"student"}
# print(dict)
# # dict.__delitem__("state")
# del dict["state"]
# print(dict)

##q8 : Create a dictionary from a list of strings, where each string becomes a key and its length becomes the value.
# list=["shivam","sumit","deepak","abhinav","avinash"]
# dict={}
# for i in list:
#     dict.update({i:len(i)})
# print(dict)

##q9 : Find the sum of all values in a dictionary that have numeric values.
# dict={"name":"shivam","age":21,"marks":95,"city":"indore"}
# sum=0
# for i in dict.values():
#     if type(i)==int:
#         sum+=i
# print("sum is : " ,sum)

##q10 : Reverse a dictionary, swapping keys and values to create a new dictionary.
# dict={"name":"shivam","age":21,"city":"gwalior","markls":98,"college":"m.i.t.s."}
# new_dict={}
# for key , values in dict.items():
#     new_dict.update({values:key})
# print(new_dict)
