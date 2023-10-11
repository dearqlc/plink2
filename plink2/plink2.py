import os
import subprocess


def getTxt():
    fil_path = "E:\WJH\wjh"
    files = os.listdir(fil_path)
    f = open("file.txt", "w")
    a = []
    for m in files:
        if str(m).__contains__("ped") and str(m).__contains__("chr"):
            a.append(int(m.split(".")[0].split("r")[1]))
    a.sort()
    for n in a:
        f.write("chr" + str(n) + str(".ped chr") + str(n).split(".")[0] + ".map\n")
    f.close()


getTxt()

for i in range(1, 3):
    subprocess.run("plink2 --bgen ukb22828_c" + str(i) + "_b0_v3.bgen ref-first --sample ukb22828_c" + str(
        i) + "_b0_v3.sample --extract 3.txt --make-pgen --out chr" + str(i) + "")
    subprocess.run("plink2 --pgen chr" + str(i) + ".pgen --pvar chr" + str(i) + ".pvar --psam chr" + str(
        i) + ".psam --export vcf")
    subprocess.run("plink2 --vcf plink2.vcf --make-bed --out chr " + str(i) + "")
    subprocess.run("plink --bfile chr" + str(i) + "--recode --out chr" + str(i) + "")
getTxt()
subprocess.run("plink --merge-list file.txt --recode --out duration")
