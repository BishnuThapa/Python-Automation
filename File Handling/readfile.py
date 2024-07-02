## file in same directory
## once you open the file its important to close the file

file=open('data.txt','r')
content=file.read() # read all lines and output
# content=file.readline() #read single line
print(content)
file.close() #closing the file