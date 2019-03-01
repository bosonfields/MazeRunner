import numpy as np
from Mazeclass import Maze
from MazeList import MazeL
import MazeList
import SearchMethod
import csv
from queue import PriorityQueue as PQ


infile = 'G:\study\Computer science\exercise-test\Mazegame\documents\input.csv'
outfile = 'G:\study\Computer science\exercise-test\Mazegame\documents\output.csv'

tmp_out_file = 'G:\study\Computer science\exercise-test\Mazegame\documents'

exportData = MazeL()
mark = 0
count = 0
while count<5:
    print("mark: ", mark)
    mark +=1
    tmp = Maze(40, 0.2 + count*0.01)
    if MazeList.detect_solvability(tmp, "A_star_manhattan"):
        exportData.ML.append(tmp)
        count +=1

exportData.write_MazeList(outfile)

'''
Numbers = np.arange(10, 520, 20)
Numbers = np.array(Numbers)

Probability = np.array([0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5])

image_Num_Prob = {}

for num in Numbers:
    for p in Probability:
        image_Num_Prob[(num, p)] = 1

for num, p in image_Num_Prob:
    image_Num_Prob[(num, p)] = SearchMethod.get_solvability(num, p)
    print(num)

tmp_export ="\\" + "Solvability.csv" + "\\"
export_p = tmp_out_file + tmp_export

with open(export_p, "w", newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Maze_dim', 'Probability_Wall', 'Probability_solvable'])
    for key in image_Num_Prob:
        num, p_wall = key
        p_solvable = image_Num_Prob[key]
        writer.writerow([np.str(num), np.str(p_wall), np.str(p_solvable)])
'''












