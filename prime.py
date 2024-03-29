# num = int(input("enter your number : "))
# check = True
# for i in range(2 , num):
#     if(num%i==0):
#         check=False
#         break
# if(check==True):
#     print("p")
# else:
#     print("np")




# Take the limits if a range from the user and count the number of prime numbers in the range

# llimit = int(input("Enter the 1st num : ")) #10
# ulimit = int(input("Enter the 2nd num : ")) #30
# count = 0
# for j in range(llimit,ulimit+1): #10
#     num = j #10
#     check = True
#     for i in range(2,num): #9
#         if(num%i==0):
#             check = False
#             break
        
#     if(check==True):
#         count+=1
#         # print(num, end=" ") 
        
    
# print("The number of prime numbers b/w",llimit ,"and",ulimit,"is",count)






llim=int(input("enter your lower limit : "))
ulim=int(input("enter your your ulim : "))
count=0
for j in range(llim, ulim):
    num=j
    check=True
    for i in range(2,num):
        if(num%i==0):
            check=False
            # print("your number is not a prime number ")
            break
    if(check==True):
        # print("your number is a prime number")
        count+=1
print("there are ",count," prime numbers are present b/w ",llim," and ",ulim)