import csv

list1 = []
wjh = csv.reader(open("E:/WJH/met.csv"))
for row in wjh:
    list1.append(row[1])
print(type(wjh))
print(list1)

# 1. 创建文件对象（指定文件名，模式，编码方式）a模式 为 下次写入在这次的下一行
with open("file.csv", "a", encoding="utf-8", newline="") as f:
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)
    # 3. 构建列表头
    # name = ["top"]
    # csv_writer.writerow(name)
    # 4. 写入csv文件内容
    for i in list1:
        csv_writer.writerow([i, "123"])
    print("写入数据成功")
    # 5. 关闭文件
    f.close()
