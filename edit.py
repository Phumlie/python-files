import os

path = "files/"
directory = os.path.dirname(path)
if not os.path.exists(directory):
    os.makedirs(directory)

fileName = "random2.gm"
file = open(path+fileName,"r")

fileName2 = "random2b.gm"
file2 = open(path+fileName2,"w+")

if file.mode == 'r':
    lines = file.readlines()
    ln = 1
    for l in lines:
        print(l.strip())
        file2.write(("%d: "%ln)+l.strip()+"\n")
        ln += 1

file.close()
file2.close()
print("Done!")
