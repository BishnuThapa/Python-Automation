# with statement handles opening and closing the file


with open("data.txt", 'r') as file:
    lines = file.readlines()

    for line in lines:
        print(line.strip())
