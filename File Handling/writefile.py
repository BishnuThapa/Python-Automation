#if there is file override content if not creates new file

#completely remove previous texts from file

with open("write.txt",'w') as file:
    file.write("This is test file")