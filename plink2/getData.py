# 将一张大的csv根据id分类成小csv

import csv


def createCsv(temp_list1):
    with open("E:\\WJH\\csvs/" + temp_list1[0].get("id") + ".csv", "a", encoding="utf-8", newline="") as f:
        csv_writer = csv.writer(f)
        name = ["chr", "beta", "id", "snp"]
        csv_writer.writerow(name)
        for i in temp_list1:
            csv_writer.writerow([i.get("chr"), i.get("beta"), i.get("id"), i.get("snp")])
        f.close()


def createTxt(snp_list1, temp_list2):
    with open("E:\\WJH\\csvs/" + temp_list2[0].get("id") + ".txt", "a", encoding="utf-8", newline="") as f:
        for i in range(0, len(snp_list1)):
            if i == len(snp_list1) - 1:
                f.write(snp_list1[i])
            else:
                f.write(snp_list1[i] + "\n")
        f.close()


met_list = []
met_csv = csv.reader(open("E:/WJH/met.csv"))
for row in met_csv:
    dict_met = {"chr": row[0], "beta": row[5], "id": row[6], "snp": row[7]}
    met_list.append(dict_met)
del (met_list[0])
id_exposure = met_list[0].get("id")
temp_list = []
snp_list = []
for met in met_list:
    if id_exposure == met.get("id"):
        temp_list.append(met)
        snp_list.append(met.get("snp"))
    else:
        createCsv(temp_list)
        createTxt(snp_list, temp_list)
        id_exposure = met.get("id")
        temp_list = [met]
        snp_list = [met.get("snp")]
createCsv(temp_list)
createTxt(snp_list, temp_list)
