#Day 2 python advanced Fri 21at
#read, write(over writes what we have in a file), append(adds things to the end of a fie)
#x9create
new = open("nnewfile.txt", "w")
new.write("I am Abdulhafiz")
new.close()

#x = open("nnewfile.txt", "r")
#print(x.read())

new = open("nnewfile.txt", "w")
new.write("Just testing")
new.close()

x = open("nnewfile.txt", "r")
print(x.read())


