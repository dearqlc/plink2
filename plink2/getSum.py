#!/user/bin/env python3
# -*- coding: utf-8 -*-
import csv

with open("nov/chr1.ped", "r") as f:
    ped_file = f.readlines()

ped_list = [i.split(" -9 ")[1].replace("\n", "") for i in ped_file]

ped_map = {i: value.split(" ") for i, value in enumerate(ped_list)}

with open("nov/Insomnia_grs.csv", "r") as f:
    csv_reader = csv.reader(f)
    csv_list = list(csv_reader)

csv_map = {i: row[5] for i, row in enumerate(csv_list[1:])}

sum_map = {}
for i, temp_list in ped_map.items():
    count = sum(x == y for x, y in zip(temp_list, csv_map.values()))
    sum_map[i] = count

print(sum_map)
