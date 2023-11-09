import csv
import os
import subprocess


# 计算总和并生成csv文件
def getTotal(map_file, csv_file, ped_file, total_file):
    list_duration = []
    f = open(map_file, "r")
    a = f.readlines()
    for n in a:
        list_duration.append(n.split("\t")[1])
    f.close()
    print(list_duration)

    # 生成snp,beta,ea键值list
    ky_list = []
    f = open(csv_file, "r")
    a = f.readlines()
    for i in a:
        row = i.split(",")
        ky_dict = {"snp": row[0], "beta": row[2], "ea": row[4]}
        ky_list.append(ky_dict)
    f.close()
    del (ky_list[0])

    list_ky1 = []
    for i in list_duration:
        for j in ky_list:
            if j.get("snp") == i:
                dict_ky1 = {"snp": j.get("snp"), "beta": j.get("beta"), "ea": j.get("ea")}
                list_ky1.append(dict_ky1)
    print(list_ky1)

    f = open(ped_file, "r")
    a = f.readlines()
    total_list = []
    for i in a:
        dna = i.split(" -9 ")[1].replace(" ", "").replace("\n", "")
        total_sum = 0
        for j in range(0, len(i.split(" -9 ")[1].replace(" ", "").replace("\n", ""))):
            if dna[j] == list_ky1[j // 2].get("ea"):
                total_sum = total_sum + float(list_ky1[j // 2].get("beta"))
        dict_temp = {"pre": i.replace("\n", ""), "total": total_sum}
        total_list.append(dict_temp)
    f.close()
    print(total_list)

    with open(total_file, "a", encoding="utf-8", newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["id", "dna", "total"])
        for i in range(0, len(total_list)):
            csv_writer.writerow([total_list[i].get("pre").split("_")[0].split(" ")[1], total_list[i].get("pre"),
                                 total_list[i].get("total")])
        f.close()


# 生成ped map对
def getTxt(file_name, id_exposure1):
    fil_path = "E:\WJH\wjh"
    files = os.listdir(fil_path)
    f = open(file_name, "w")
    txt_list = []
    for m in files:
        if str(m).__contains__("ped") and str(m).__contains__("chr") and str(m).__contains__(id_exposure1):
            txt_list.append(int(m.split(".")[0].split("r")[1]))
    txt_list.sort()
    for n in txt_list:
        f.write("chr" + str(n) + str(".ped chr") + str(n).split(".")[0] + ".map\n")
    f.close()


# 载入met.csv
met_list = []
met_csv = csv.reader(open("file/met.csv"))
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

# 大循环
for id_exposure in id_list:
    # 小循环
    for chr_exposure in chr_dict.get(id_exposure):
        subprocess.Popen(
            "plink2 --bgen ukb22828_c" + str(chr_exposure) + "_b0_v3.bgen ref-first --sample ukb22828_c" + str(
                chr_exposure) + "_b0_v3.sample --extract 3.txt --make-pgen --out chr" + str(chr_exposure) + "").wait()
        subprocess.Popen(
            "plink2 --pgen chr" + str(chr_exposure) + ".pgen --pvar chr" + str(chr_exposure) + ".pvar --psam chr" + str(
                chr_exposure) + ".psam --export vcf").wait()
        subprocess.Popen("plink2 --vcf plink2.vcf --make-bed --out chr " + str(chr_exposure) + "").wait()
        subprocess.Popen("plink --bfile chr" + str(chr_exposure) + "--recode --out chr" + str(chr_exposure) + "").wait()
    getTxt(id_exposure + ".txt", id_exposure)
    subprocess.Popen("plink --merge-list " + id_exposure + ".txt --recode --out duration").wait()
    getTotal(id_exposure + ".map", id_exposure + ".csv", id_exposure + ".ped", id_exposure + "_result.csv")
