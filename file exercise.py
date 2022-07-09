import fileinput
f=open("example.txt",'w')
f.write("this is my first file")
f.write("my first file project in python")
f.write("i am ashish")
f.close()

f=open("example.txt",'r')
print(f.read())
f.close()

f=open("example.txt","r")
for i in f:
    print(i)
f=open("example.txt","r")
print(f.read())


f=open("example.txt","r")
x=f.readlines()
print(x)

f=open("example.txt","a")
f.write("this value i have appended")
f.close()

f=open("example.txt","r")
print(f.read(9))
f.close()

f=open("example.txt", "r+")
print(f.read())
f.write("thanks ")
f.close()

