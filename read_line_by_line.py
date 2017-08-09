import os

path = "files/"
directory = os.path.dirname(path)
if not os.path.exists(directory):
    os.makedirs(directory)

fileName = "random2.gm"
file = open(path+fileName,"r")

if file.mode == 'r':
    lines = file.readlines()
    for l in lines:
        print(l.strip())

file.close()
print("Done!")
