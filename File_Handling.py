# Reading a file
file=open("file1.txt","r")
c=file.read()
print(c)
# Writing to a file
file=open("file1.txt","w")
file.write("I also learn coding in my free time\n")
file.close()
# append the data to the existing file
file=open("file1.txt","a")
file.write("I also play on my console")
file.close()
