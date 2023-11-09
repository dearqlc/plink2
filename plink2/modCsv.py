#!/user/bin/env python3
# -*- coding: utf-8 -*-
import csv


def createCsv(temp_list1):
    with open("file/met1.csv", "a", encoding="utf-8", newline="") as f:
        csv_writer = csv.writer(f)
        name = ["chr.exposure", "samplesize.exposure", "se.exposure", "pos.exposure", "pval.exposure", "beta.exposure",
                "id.exposure", "SNP", "effect_allele.exposure", "other_allele.exposure", "eaf.exposure", "exposure"]
        csv_writer.writerow(name)
        for i in temp_list1:
            if float(i.get("beta.exposure")) < 0:
                csv_writer.writerow(
                    [i.get("chr.exposure"), i.get("samplesize.exposure"), i.get("se.exposure"), i.get("pos.exposure"),
                     i.get("pval.exposure"), str(i.get("beta.exposure")).replace("-", ""), i.get("id.exposure"), i.get("SNP"),
                     i.get("other_allele.exposure"), i.get("effect_allele.exposure"), i.get("eaf.exposure"), i.get("exposure")])
            else:
                csv_writer.writerow(
                    [i.get("chr.exposure"), i.get("samplesize.exposure"), i.get("se.exposure"), i.get("pos.exposure"),
                     i.get("pval.exposure"), i.get("beta.exposure"), i.get("id.exposure"), i.get("SNP"),
                     i.get("effect_allele.exposure"), i.get("other_allele.exposure"), i.get("eaf.exposure"), i.get("exposure")])
        f.close()


met_list = []
met_csv = csv.reader(open("file/met.csv"))
for row in met_csv:
    dict_met = {"chr.exposure": row[0], "samplesize.exposure": row[1], "se.exposure": row[2], "pos.exposure": row[3],
                "pval.exposure": row[4], "beta.exposure": row[5], "id.exposure": row[6], "SNP": row[7],
                "effect_allele.exposure": row[8], "other_allele.exposure": row[9],
                "eaf.exposure": row[10], "exposure": row[11]}
    met_list.append(dict_met)
del (met_list[0])
id_exposure = met_list[0].get("id")
temp_list = []
snp_list = []
for met in met_list:
    temp_list.append(met)
createCsv(temp_list)
