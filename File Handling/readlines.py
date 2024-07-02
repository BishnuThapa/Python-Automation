
file=open("data.txt",'r')
lines=file.readlines()


#each line takes new line character on loop
for line in lines:
    print(line)

# to remove spaces between lines 
for line in lines:
    print(line.strip())

file.close()