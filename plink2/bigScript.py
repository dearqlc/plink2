import csv

# 载入met.csv
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

# 大循环
for id_exposure in id_list:
    # 小循环
    for chr_exposure in chr_dict.get(id_exposure):
        pass
