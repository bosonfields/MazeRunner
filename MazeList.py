import numpy as np
import csv
from Mazeclass import Maze
import SearchMethod

class MazeL():
    ML = list()
    def __init__(self, mazelist =[]):
        self.ML = mazelist
    def add_Maze(self, maze):
        self.ML.append(maze)
    def __iter__(self):
        return self.ML
    def __next__(self):
        return self.ML

    def write_MazeList(self, outfile):
        with open(outfile, "w", newline='') as csvFile:
            writer = csv.writer(csvFile)
            for maze in self.ML:
                dim = maze.dim
                writer.writerow(['Maze_dim', np.str(dim)])
                tmp_maze = np.array(maze.M, copy=True)
                tmp_maze.astype(str)
                writer.writerows(tmp_maze)

def read_MazeList(MazeList, infile):
    with open(infile, 'r') as csvFile:
        tmp = csv.reader(csvFile, delimiter=',')
        tmp_input = list(tmp)
    while tmp_input:
        if tmp_input[0][0] == "Maze_dim":
            dim = np.int(tmp_input[0][1])
            tmpMaze = Maze(dim)
            tmp_input.pop(0)
            data = []
            for item in range(dim):
                tmp_data = [int(float(x)) for x in tmp_input.pop(0)]
                data.append(tmp_data)
            ndata = np.array(data)
            tmpMaze.M = ndata
            MazeList.append(tmpMaze)

def get_solvable_maze(MazeList):
    begin  =(0,0)
    for maze in MazeList:
        path, history = SearchMethod.A_star_heuristic_only(begin, maze)
        if not path:
            MazeList.remove(maze)

def detect_solvability(Maze, method):
    begin  =(0,0)
    sol = True
    path =[]
    history = []
    Max_fringe = 1
    if method == "A_star_Manhattan":
        path, history, Max_fringe = SearchMethod.A_star_Manhattan(begin, Maze)
    if method == "DFS_oriented":
        path, history, Max_fringe = SearchMethod.DFS_oriented(begin, Maze)
    if not path:
        sol = False
    return sol, path, history, Max_fringe







