import csv
import os
import subprocess

met_list = []
met_csv = csv.reader(open("met.csv"))
for row in met_csv:
    dict_met = {"chr": row[0], "id": row[6]}
    met_list.append(dict_met)
del (met_list[0])

# 获取大小循环列表
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

def getTxt():
    fil_path = "E:/imputation"
    files = os.listdir(fil_path)
    f = open("file_" + id_exposure+ ".txt", "w")
    a = []
    for m in files:
        if str(m).__contains__("ped") and str(m).__contains__("chr"):
            a.append(int(m.split(".")[0].split("r")[1]))
    a.sort()
    for n in a:
        f.write("chr" + str(n) + "_" + id_exposure + " " + str(".ped chr") + str(n).split(".")[0] + "_" + id_exposure + ".map\n")
    f.close()


subprocess.Popen("plink2.exe").wait()
subprocess.Popen("plink.exe").wait()

getTxt()
subprocess.Popen("plink --merge-list file_" + id_exposure+ ".txt --recode --out "+ id_exposure).wait()