f = open('/Users/babs/Documents/listnum1.txt', 'r')
f2 = open('/Users/babs/Documents/listnum2', 'r')
f1_data=f.readlines()
f2_data=f2.readlines()
# print(f1_data)
# print(f2_data)
for i in f1_data:
    if i in f2_data:
        pass
    else:
      with open('savefile.txt','a')as j:
          j.write(i+'\n')




# closing files
f.close()
f2.close()


# readfile=open('/Users/babs/Documents/zen2.txt','r')
# for line in readfile:
#     print(line,end='')
# readfile=open('/Users/babs/Documents/zen.txt','r')
# for line in readfile:
#     if line.startswith('Beautiful') is True:
#         with open('/Users/babs/Documents/answer.txt','a') as File:
#             File.write(line)


# f = open('/Users/babs/Documents/listnum1.txt', 'r')
# f2 = open('/Users/babs/Documents/listnum2', 'r')
# f1_data=f.readlines()
# f2_data=f2.readlines()
# print(f1_data)
# print(f2_data)
# for element in f1_data:
#     if element not in f2_data:
#

