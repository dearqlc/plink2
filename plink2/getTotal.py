# 获取rs
import csv

list_duration = []
f = open("file/duration.map", "r")
a = f.readlines()
for n in a:
    list_duration.append(n.split("\t")[1])
f.close()
print(list_duration)

# 生成snp,beta,ea键值list
ky_list = []
f = open("file/sleepduration.csv", "r")
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

f = open("duration2.ped", "r")
a = f.readlines()
total_list = []
total_sum = 0
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

with open("total.csv", "a", encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["id", "dna", "total"])
    for i in range(0, len(total_list)):
        csv_writer.writerow([total_list[i].get("pre").split("_")[0].split(" ")[1], total_list[i].get("pre"),
                             total_list[i].get("total")])
    f.close()
