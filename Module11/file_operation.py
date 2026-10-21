#Opening and Closing Files
#file_path = "example.txt"
#file = open(file_path, "r")

#content = file.read()
#print(content)

#file.close()

import os

file_path = "example.txt"
file = open(file_path, "r")

#with open('example.txt', 'r') as file:
    #content = file.read()
    #line = file.readline()
    #lines = file.readlines()


    #print(content)
    #print(line)
    #print(lines)

#'r' = read
#'w' = write
#'a' = append
#'wb' = binary mode
#'x' = exclusive creation

with open('example.txt', 'w') as file:
    file.write("Writing into file")

lines = ['Hello World!\n', 'Welcome to Python!\n']
with open('example.txt', 'w') as file:
    file.writelines(lines)

if os.path.exists("example.txt"):
    print("File exists")

with open('example.txt', 'a') as file:
    file.write("New data appended")

data = b'This is some binary data'
with open('example.bin', 'wb') as file:
    file.write(data)

with open("binary_bin.bin", "rb") as binary_file:
    data = binary_file.read()