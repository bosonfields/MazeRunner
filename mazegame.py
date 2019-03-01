import SearchMethod
from Mazeclass import Maze
import numpy as np
from MazeList import MazeL
import MazeList as ML
import time
import sys
import csv


sys.setrecursionlimit(100000000)

test = Maze(400, 0.2)
begin = (0, 0)
time_start = time.clock()
'''
infile = 'G:\study\Computer science\exercise-test\Mazegame\documents\input.csv'
tmp_out_file = 'G:\study\Computer science\exercise-test\Mazegame\documents'

testTime = []
ML.read_MazeList(testTime, infile)

begin = (0,0)
DFS_record = []
DFS_M_record = []
records = []

for j in range(200):
    maze = testTime[j]
    print("This is map: ", j)
    dim = maze.dim
    time_start_DFS= np.double(time.clock())
    path_DFS, history_DFS = SearchMethod.DFS_default((0,0), maze)
    time_end_DFS =np.double(time.clock())
    DFS_record.append((str(dim), str(time_end_DFS - time_start_DFS), str(len(path_DFS)), str(len(history_DFS))))
    print("Time of DFS: ", time_end_DFS - time_start_DFS, "path length: ", len(path_DFS), "visited nodes:", len(history_DFS))
    time_start_DFS_M = np.double(time.clock())
    path_DFS_M, history_DFS_M = SearchMethod.DFS_oriented((0, 0), maze)
    time_end_DFS_M = np.double(time.clock())
    DFS_M_record.append((str(dim), str(time_end_DFS_M - time_start_DFS_M), str(len(path_DFS_M)), str(len(history_DFS_M))))
    print("Time of BFS: ", time_end_DFS_M - time_start_DFS_M, "path length: ", len(path_DFS_M), "visited nodes:", len(history_DFS_M))
    records.append((str(dim), str(time_end_DFS - time_start_DFS), str(len(path_DFS)), str(len(history_DFS)),
                    str(time_end_DFS_M - time_start_DFS_M), str(len(path_DFS_M)), str(len(history_DFS_M))))


tmp_export_DFS ="\\" + "DFS_DFS.csv" + "\\"
export_p_DFS = tmp_out_file + tmp_export_DFS

with open(export_p_DFS, "w", newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Maze dim','Time cost_D', 'path length_D', 'visited nodes_D', 'Time cost_D_M', 'path length_D_M', 'visited nodes_D_M'])
    for r in records:
        writer.writerow(r)

'''
#path, history, Max_fringe = SearchMethod.DFS_default(begin, test)
#path, history = SearchMethod.BFS(begin, test)
#path, history = SearchMethod.A_star_Euclidean(begin, test)
path, history, Max_fringe = SearchMethod.A_star_Manhattan(begin, test)
#path, history = SearchMethod.A_star_heuristic_only(begin, test)
#path_find = time.clock()

#print("Start time: ", time_start)
#print("Finding Path time: ", path_find)

if not path:
    print("There is no route to solve the problem")
    print("Search history is: ", history)
    print("Maximum fringe is:", Max_fringe)
    test.show_figure(history)
else:
    print("There is a path exist from start to end")
    print("Path record is: ", path)
    print("history length: ", len(history))
    print("path length", len(path))
    print("Maximum fringe is:", Max_fringe)
    test.show_figure(path)






