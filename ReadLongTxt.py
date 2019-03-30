import time
import os.path
import shutil

# -*- coding: utf-8 -*-
start_time = time.clock()
#
# f = open("C:/Users/Khrul Sergey/Downloads/QAtest/QAtest.txt", encoding="utf8")
#
# row_index = 0
# count_of_a = 0
#
# line = f.readline()
# while line:
#     row_index += 1
#     for litera in line:
#         if litera == 'a':
#             count_of_a += 1
#     line = f.readline()
#
# print("--- %s seconds ---" % (time.clock() - start_time))
# print("Row count =", row_index, "  Count of symbol 'a' = ", count_of_a)
#
# f.close()
#
# d = {
#     'os': {
#         'type': 'windows',
#         'version': '8.1'
#     },
#     'browser': {
#         'type': 'chromw',
#         'version': '56.1'
#     }
# }

os.getcwd()
os.chdir("c:/tools")
os.listdir(".")
os.mkdir('tools')
os.makedirs('test/test1/test2')
os.rmdir('tools')
shutil.rmtree('test')
shutil.copy('c:/windows/temp.txt', 'c:/tools/temp.txt')
os.remove('temp.txt')
os.path.isfile('tools')
os.path.isdir('gff')
s = list(filter(lambda f: os.path.isfile(f), os.listdir('.')))
