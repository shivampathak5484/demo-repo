# count=0
# for i in range(0,1000):
#     num=i
#     digits=0
#     t=num
#     while(t>0):
#         t//=10
#         digits+=1
#     t2=num
#     sum=0
#     while(t2>0):
#         rem=t2%10
#         product=1
#         for j in range(0,digits):
#             product*=rem
#         sum+=product
#         t2//=10
#     if(num==sum):
#         count+=1
#         print(num)


# count=0
# for i in range(0,100000):
#     num=i
#     digit=0
#     t1=num
#     while(t1>0):
#         t1//=10
#         digit+=1
#     t2=num
#     sum=0
#     while(t2>0):
#         rem=t2%10
#         product=1
#         for j in range(0,digit):
#             product*=rem
#         sum+=product
#         t2//=10
#     if(num==sum):
#         count+=1
#         print(num)

# print("there are ",count," numbers are amstrong number between your limit")



count=0
llim=int(input("enter your lower limit : "))
ulim=int(input("enter your upper limit : "))
for i in range(llim,ulim):
    num=i
    digit=0
    t=num
    while(t>0):
        t//=10
        digit+=1
    t2=num
    sum=0
    while(t2>0):
        rem=t2%10
        product=1
        for j in range(0,digit):
            product*=rem
        sum+=product
        t2//=10
    if(num==sum):
        count+=1
        print(num)