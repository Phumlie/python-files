import os

path = "files/"
directory = os.path.dirname(path)
if not os.path.exists(directory):
    os.makedirs(directory)

fileName = "random2.gm"
file = open(path+fileName,"r")

if file.mode == 'r':
    contents = file.read()
    print(contents)

file.close()
print("Done!")
