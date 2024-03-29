# a1={"name":"shivam ","grades":"a"}  
# a2={"name":"suruchi","grades":"b"}
# a3={"name":"manvendra","grades":"c"}
# a4={"name":"satyarth","grades":"a++"}
# students={"a1":{"name":"shivam ","grades":"a"},"a2":{"name":"suruchi","grades":"b"},"a3":{"name":"manvendra","grades":"c"},"a4":{"name":"satyarth","grades":"a++"}}
# # list=[a1,a2,a3,a4]
# for i in students.items():
#     for j in i[1].values():
#             print(j)






'''Values can be in the form of list or tuple or dictionary'''
'''but keys can only be in the form of integers or string and must be immutable'''


# # Create a dictionary with key-value pairs
# person = {"name": "Alice", "age": 30, "city": "New York"}


# #Accessing values using key
# print(person["city"])
# student = {"rohan":"pizza" , "aman":"burger" , "simran":"dosa" , "sunaina":"shake" , "kashish":{"breakfast":"pasta", "lunch":"chowmien", "dinner":"momos"}}
# print(student["kashish"]["lunch"])


# # Adding new key-value pairs
# person["ph_number"] = "8103221865" #both are same
# person.update({"occupation":"barber"}) #both are same
# print(person)


# # # Modifying existing values
# person["age"] = 31
# print(person)
# print(type(person))
# print(student.get('kashish'))


# # # Checking for key existence
# if "age" in person:
#     print("The 'age' key exists")
# # # Looping through a dictionary (keys and values)
# for key, value in person.items():
#     print(f"{key}: {value}")




    
        

    
    
