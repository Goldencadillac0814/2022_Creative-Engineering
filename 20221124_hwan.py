# sum = 0
# for i in range(1, 101):
#     if i%3 ==0:
#         sum = sum +i
#         print("i = ",i,"/ sum = ",sum)
#     if sum > 250:
#         break
# print(sum)



# sum = 0
# for i in range(1, 101):
#     if i%3 ==0: #and sum <= 250:
#         sum = sum +i
#         print("i = ",i,"/ sum = ",sum)

# print(sum)



# arr = []
# for i in range(1, 11):
#     arr.append(10*i)
#     print(arr[i-1])
# arr[5] = 500
# print(arr)



# a = int(input())
# b = int(input())
# for i in range(a+1, b):
#     print(i)

import random
ten = []
for i in range(10):
    ten.append(random.randint(0,1000))
print(ten)
print(max(ten), min(ten))