import os

path = "files/"
directory = os.path.dirname(path)
if not os.path.exists(directory):
    os.makedirs(directory)

fileName = "random2.gm"
file = open(path+fileName,"a+")

for i in range(5):
    n = (i+1)*2
    file.write("This is appended line number %d\n" % n)

file.close()
print("Done!")
