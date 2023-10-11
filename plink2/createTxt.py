import os

fil_path = "E:/long"
files = os.listdir(fil_path)
a = []
for m in files:
    if str(m).__contains__("ped"):
        a.append(int(m.split(".")[0].split("r")[1]))
a.sort()
f = open("file.txt", "w")
for n in a:
    f.write("chr" + str(n) + str(".ped chr") + str(n).split(".")[0] + ".map\n")
f.close()
print(a)
