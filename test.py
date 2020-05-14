# f = open("C:\\Users\\lenovo\\Desktop\\曲线单位.txt", "r")
# i = open("C:\\Users\\lenovo\\Desktop\\曲线单位.txt", "r")
# line_num = 0
# name = None
# lines = i.readlines()
# line = f.readlines()
# count = len(line)
#
# while line_num < count:
#     lines_num = 0
#     num = 0
#     while lines_num < count:
#         if line[line_num] == lines[lines_num]:
#             num += 1
#         if num > 1:
#             if line[line_num] != name:
#                 print("%s出现%s次" % (line[line_num], num))
#             name = line[line_num]
#         lines_num += 1
#     line_num += 1
# if name is None:
#     print("文件不存在重复项！")
from selenium.webdriver.common.by import By

a = eval("By.CSS_SELECTOR, 'div[index=\"%s\"] input', \"3\"")
print(tuple(a)[2])