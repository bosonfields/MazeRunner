import numpy as np
from Mazeclass import Maze
from MazeList import MazeL
import SearchMethod
import csv
import matplotlib.pyplot as plt

infile = 'G:\study\Computer science\exercise-test\Mazegame\documents\plot2.csv'
tmp_out_file = 'G:\study\Computer science\exercise-test\Mazegame\documents'

'''
a = np.loadtxt(infile, dtype=np.str, delimiter=",")
b = a[1:,:].astype(np.float)

data_list =[]
tmp = np.zeros((1,6))
set_dim = 50
count = 0

for i in range(105):
    if i+1 == 105:
        tmp = tmp / count
        tmp = np.append(tmp, set_dim)
        data_list.append(tmp)
        count = 0
        tmp = np.zeros((1, 6))
        set_dim = b[i, 0]
    if set_dim == b[i,0]:
        count +=1
        tmp = tmp + b[i,1:]
    else:
        tmp = tmp/count
        tmp = np.append(tmp, set_dim)
        data_list.append(tmp)
        count =0
        tmp = np.zeros((1,6))
        set_dim = b[i,0]


tmp_export ="\\" + "average_DFS_DFS_M.csv" + "\\"
export_p = tmp_out_file + tmp_export

with open(export_p, "w", newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['DFS Time', 'DFS path',  'DFS History','BFS Time', 'BFS Path', ' BFS History', 'Maze number'])
    for key in data_list:
        writer.writerow([np.str(key[0]), np.str(key[1]), np.str(key[2]), np.str(key[3]), np.str(key[4]), np.str(key[5]), np.str(key[6])])

'''
a = np.loadtxt(infile, dtype=np.str, delimiter=",")
z = a[1:,:].astype(np.float)

b = np.zeros((1,10))

for i in range(28):
    b = b + z[i*10:(i+1)*10,2]

b=b/28
print(b)

b[0][-1] = 0
b[0][-2] = 0

print(b)

P_solvability = b[0]
P_generate_wall = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]

simulate = np.polyfit( P_solvability, P_generate_wall, 2)
Fitting = np.poly1d(simulate)
p_0 = Fitting(0.35)
print(p_0)
print(Fitting)

'''


data_P0 = {}

for item in dim_list:
    dim = np.int(item)
    tmp = data_list[item]
    y = tmp[0:10,0]
    x = tmp[0:10,1]
    f1 =np.polyfit(x,y, 3)
    p1 = np.poly1d(f1)
    fp0 = p1(0.5)
    data_P0[dim] = fp0

print(data_P0)

dim = list(data_P0.keys())
p0 = list(data_P0.values())

f2 = np.polyfit(dim, p0, 2)
p2 = np.poly1d(f2)

p0_var =p2(dim)
print(p2)

tmp_export ="\\" + "Fitting_pp.csv" + "\\"
export_p = tmp_out_file + tmp_export

with open(export_p, "w", newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Maze_dim', 'Fitting_P0'])
    for key in data_P0:
        writer.writerow([np.str(key), np.str(data_P0[key])])

'''

