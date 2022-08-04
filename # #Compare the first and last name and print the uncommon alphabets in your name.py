# #Compare the first and last name and print the uncommon alphabets in your name
print("enter your first name")
str1=str(input())
print("enter your last name")
str2=str(input())
l=[]

for item in str1:
    if item not in str2:
        l.append(item)
for item in str2:
    if item not in str1:
        l.append(item)
print(l)
