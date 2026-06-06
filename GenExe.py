# set1={1,4,2,3,8,10,9}
# print(set1)
# set2=[4 in set1]
# print(set2)
# se_2=set(range(1,10,2))
# print(se_2)
# set3=set1&se_2
# print(set3)
from array import*

# nums= int(input("enter your number: "))
# for i in range(nums):
#     for y in range(i):
#         print(i,y,end="")
#     print()
#
# num= int(input("enter your number: "))
# for i in range(num):
#     for y in range(i+1):
#         print('*', end="")
#     print()
#
# for i in range(4):
#     for j in range(4):
#         print('*',end=' ')
#     print()
#
# vals=array('i',[1,4,6,7,8,9])
# print(vals)
# vals_new=vals.tolist()
# vals_new.sort()
# print()
# #newarr=array(vals.typecode,(a*a for a in vals))
# for v in vals:
#     print(v)
# print(vals_new)
#
# num=6
# for i in range(num-1,0,-1):
#     print(i)

import random

for x in range(1,21):
    if x%5!=0:
        pass
    else:
        print(x)

word_list = ["python", "hangman", "programming", "challenge"]
secret_word = random.choice(word_list)
print(secret_word)