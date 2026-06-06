mixed_case= "A Song of Ice and Fire"
print(mixed_case.isupper())
print(mixed_case.islower())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.istitle())
title_case= mixed_case.title()
print(title_case)
print(mixed_case.startswith("A"))
print(mixed_case.endswith("Fire"))
words = ("Mango","Milk","Sweet","fruits")
print(" ".join(words))
print(",".join(["Mango","Milk","Sweet","fruits"]).isalpha())
print("".join(words).isalpha())
print(words)
first=10.1
second=20
sum= first+float(second)
print(sum)
