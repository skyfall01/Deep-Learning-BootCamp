
import os
os.system("cls")

#create new file and close
f = open("newfile1.txt","w+")
f.close()

#write something to above created file and close
f = open("newfile1.txt","w")
f.write("sdfsdfsdf sdfsdf\nsdfsdfsdf")
"""
Only strings can be written to a file. 
Typecast other data-type to strings - str()
Only in read/append mode only.(not applicable to binary files)
"""
f.close()

#read from file
f = open("newfile1.txt","r")
f1 = open("newfile.txt","a")
p1 = f.read()#read every line as string
print(p1)
for i in p1:
    f1.write(i) #copy contents from p1 and append to f1
f1.close()
p = f.readlines()#read all lines and form a list
print(p) 
f.close()

#To read images/binary files
f = open("pic.png","rb") #"wb" to write to binary file
p = f.read()
print(p)
f.close()


