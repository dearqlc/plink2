# ����met.csv
import csv
import os
import subprocess

met_list = []
met_csv = csv.reader(open("met.csv"))
for row in met_csv:
    dict_met = {"chr": row[0], "id": row[6]}
    met_list.append(dict_met)
del (met_list[0])

# ��ȡ��Сѭ���б�
chr_dict = {}
chr_set = set()
id_list = [met_list[0].get("id")]
id_exposure = met_list[0].get("id")
for met in met_list:
    if id_exposure == met.get("id"):
        chr_set.add(int(met.get("chr")))
    if id_exposure != met.get("id"):
        chr_dict.setdefault(id_exposure, sorted(list(chr_set)))
        chr_set = set()
        chr_set.add(int(met.get("chr")))
        id_exposure = met.get("id")
        id_list.append(id_exposure)
chr_dict.setdefault(id_exposure, sorted(list(chr_set)))


# ����map ped��ֵ��
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


# ��ѭ��
for id_exposure in id_list:
    # Сѭ��
    for chr_exposure in chr_dict.get(id_exposure):
        subprocess.Popen(
            "plink2 --bgen ukb22828_c" + str(chr_exposure) + "_b0_v3.bgen ref-first --sample ukb22828_c" + str(
                chr_exposure) + "_b0_v3.sample --extract 3.txt --make-pgen --out chr" + str(chr_exposure) + "").wait()
        subprocess.Popen(
            "plink2 --pgen chr" + str(chr_exposure) + ".pgen --pvar chr" + str(chr_exposure) + ".pvar --psam chr" + str(
                chr_exposure) + ".psam --export vcf").wait()
        subprocess.Popen("plink2 --vcf plink2.vcf --make-bed --out chr " + str(chr_exposure) + "").wait()
        subprocess.Popen("plink --bfile chr" + str(chr_exposure) + "--recode --out chr" + str(chr_exposure) + "").wait()
    getTxt()
