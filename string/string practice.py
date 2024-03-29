##q1 : Extract the first three characters from the string "Python".
# str= "my name is shivam pathak "
# print(str[0:3])

##q2 : Extract the last two characters from the string "Programming".
# str="programming"
# print(str[len(str)-2:len(str):])

##q3 : Extract characters from index 2 to index 5 (inclusive) from the string "HelloWorld".
# str="helloWorld"
# print(str[2:6])

##q4 : Extract every second character from the string "Education".
# str="Education"
# print(str[0:len(str):2])

##q5 (: Reverse the string "Hello" using slicing.
# str="hello"
# print(str[::-1])

##q6 : Create a new string with the first and last characters of the string "JavaScript".
# str="JavaScript"
# new_str=str[0:1]+str[len(str)-1:len(str)-2:-1]
# print(new_str)

##q7 : Check if the string "Python" is a substring of the string "I love Python programming".
# str=input("enter your string : ")
# str1="i love python programming"
# if str in str1:
#     print("yes")
# else:
#     print("no")

##q8 : Split the string "Welcome to Python" into a list of words.
# str="Welcome to Python"
# list=[]
# for i in str:
#     list.append(i)
# print(list)

##q9 : Replace all occurrences of the letter "o" with the letter "a" in the string "Coding is fun".
# str="coding is fun"
# print(str.replace("o","a",-1))

##q10 : Create a new string by interleaving the characters of two strings, "Python" and "Programming", like "Pyrgomamrnoitnhgan".

##q11 : Extract the middle three characters from the string "HelloWorld".

##q12 : Print a string in reverse order, one character per line.
# str="python"
# for i in str[::-1]:
#     print(i)

##q13 : Extract the first and last two characters of each word in the string "Python Programming".

##q14 : Check if a string is a palindrome (reads the same backward as forward) using slicing.
# str=input("enter your string : ")
# rev_str=str[::-1]
# if str == rev_str:
#     print("yes your string is a palindrome ")
# else:
#     print("no your string is not a palindrome ")

##q15 : Create a list of all unique characters in a string, preserving their order of appearance.
# str=input("enter your string : ")
# list=[]
# for i in str:
#     if i not in list:
#         list.append(i)
# print(list)


##1. Write a function to check if two strings are anagrams.
# str1=input(" enter your first string here : ")
# str2=input("enter your second string here : ")
# check=True
# for i in str1:
#     if i not in str2:
#         check=False
#         print("no")
#         break
# if check==True:
#     print("yes")


##2. Given a paragraph, count the frequency of each word and display the top N frequent words.
# x="my name is shivam pathak my my my my name name name is sivam pathak"
# y=x.split(" ")
# z={}
# for i in y:
#     if i not in z:
#         z[i]=1
#     else:
#         z[i]+=1
# print(max(z.values()))
# for i in z.items():
#     print(i)



##3. Find the length of the longest substring without repeating characters in a given string.
# str="my name is shivam pathak and i am an engineer abcdefghi "
# x=str.split(" ")
# print(x)
# h=0
# for i in x:
#     j=i
#     g=[]
#     for k in j:
#         if k not in g:
#             g.append(k)
#     z=len(g)
#     if len(g)>h:
#         h=len(g)
# print(h)

##4. Given a string and a substring, find all occurrences of the substring that are anagrams.
# a="my name is shivam pathak "
# b="kahtap"
# i = a.split(" ")
# count=0
# for j in i:
#     check=True
#     for i in b:
#         if i not in j:
#             check=False
#             break
#     if check==True:
#         count+=1
# print(count)

# a="my name is suruchi sahu"
# b="ihcurus"
# i = a.split(" ")
# count=0
# for j in i:
#     for i in b:
#         if i not in j:
#             break
#     else:
#         count+=1
# print(count)

##5. Find the longest palindromic substring in a given string


