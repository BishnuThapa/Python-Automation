with open("write.txt",'a') as file:
    file.write("This is second line")

    # we can append multiple line with writelines method on python

lines=['Third append\n','Fourth Line to append \n']
with open("write.txt", 'a') as file:
    file.writelines(lines)
