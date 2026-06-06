# def tri_recursion(k):
#   if k > 0:
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("Recursion Example Results:")
# tri_recursion(6)



# def tro_recursion(x):
#   if x>0:
#     result = x + tro_recursion(x-1)
#     print(result)
#   else:
#     result=0
#   return result
  
# print("Recursion Example Results:")
# tro_recursion(6)

# names=["john","femi","tunde","joy"]
# caps_words=list(map(lambda x: x.upper(),names))
# print(caps_words)


# nums = [1, 2, 3, 4]
# squared = (map(lambda x: x**2, nums))
# print(list(squared))  # [1, 4, 9, 16]


# nums=[1,4,7,13,16,11]
# fil_nums=list(filter(lambda x:x>10, nums))
# print(fil_nums)

# students = [
#     ("john", 45),
#     ("linda", 78),
#     ("femi", 52),
#     ("tunde", 30),
#     ("joy", 80)
# ]


# fil_std=filter(lambda x: x[1]>=50, students)

# uppercased=map(lambda s: s[0].upper(), fil_std)
# final_result= list(uppercased)
# print(final_result)


people = [("Alice", 28), ("Bob", 35), ("Cynthia", 24)]

name= map(lambda x: x[0].upper(),people)
result=list(name)
print(result)


