import os

path = "files/"
directory = os.path.dirname(path)
if not os.path.exists(directory):
    os.makedirs(directory)

fileName = "random.gm"
file = open(path+fileName,"w+")
file.close()
