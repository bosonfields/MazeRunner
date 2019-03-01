import numpy as np
import SearchMethod
import MazeList
from MazeList import MazeL
from Mazeclass import Maze


def pair_changes(maze, pair, heuristic, method):
    if pair:
        blank, block = pair
        recite_x = maze.M[block]
        recite_y = maze.M[blank]
        maze.M[block] = 0
        maze.M[blank] = 1
        sol, path, history, Max_fringe = MazeList.detect_solvability(maze, method)
        tmp_heuristic = weight(maze.dim, path, history, Max_fringe)
        if sol and tmp_heuristic> heuristic:
            return tmp_heuristic
        else:
            maze.M[block] = recite_x
            maze.M[blank] = recite_y
            return heuristic

def weight(dim, path, history, Max_fringe):
    path_len = float(len(path))
    history_len = float(len(history))
    return  Max_fringe/dim

def beam_initial(maze_list, num_trials = 100, pair =((0,0),(0,0)), method = 'A_star_Manhattan', infile = " "):
    if infile == " ":
        dim = len(maze_list[0].M)
        beam_search(maze_list, dim, num_trials, pair, method)

def beam_search(maze_list, dim, num_trials, pair, method):
    optimized_maze_list = []
    maze_heuris_dict = {}
    initial_heuristic = []
    every_largest_heuristic = []
    tmp_heuristic = []
    for maze in maze_list:
        sol, path, history, Max_fringe = MazeList.detect_solvability(maze, method)
        maze_heuris_dict[maze] = weight(dim, path, history, Max_fringe)
        initial_heuristic.append(maze_heuris_dict[maze])
    while maze_list:
        Node_trials = {}
        for maze in maze_list:
            Max_weight = maze_heuris_dict[maze]
            for i in range(num_trials):
                test = Maze(maze.dim)
                test.M = maze.M.copy()
                tmp_change = test.random_change_pairs()
                sol, path, history, Max_fringe = MazeList.detect_solvability(test, method)
                tmp_weight = weight(dim, path, history, Max_fringe)
                print("for ",i,"th time: the tmp_weight is", tmp_weight,"and the Max_weight is:", Max_weight)
                if sol and tmp_weight > Max_weight:
                    print("Mark")
                    Node_trials[tmp_change] = tmp_weight
                    Max_weight = tmp_weight
            if Max_weight == maze_heuris_dict[maze]:
                optimized_maze_list.append(maze)
                every_largest_heuristic.append(Max_weight)
                maze_list.remove(maze)
        if Node_trials:
            next_step = max(Node_trials, key=Node_trials.get)
            for maze in maze_heuris_dict:
                maze_heuris_dict[maze] = pair_changes(maze, next_step, maze_heuris_dict[maze], "A_star_manhattan")
                tmp_heuristic.append(maze_heuris_dict[maze])
            print("The max in this run is: ", max(tmp_heuristic))
        else:
            return optimized_maze_list, maze_heuris_dict, initial_heuristic, every_largest_heuristic

    return optimized_maze_list, maze_heuris_dict, initial_heuristic, every_largest_heuristic


infile = 'G:\study\Computer science\exercise-test\Mazegame\documents\input.csv'
tmp_out_file = 'G:\study\Computer science\exercise-test\Mazegame\documents'


testTime = []
MazeList.read_MazeList(testTime, infile)

testTime[0].show_figure()

optimized_maze_list, maze_heuris_dict, initial, middle = beam_search(testTime, 40, 400, ((0,0),(0,0)), 'A_star_Manhattan')

print("initial: ", max(initial), "middle: ", max(middle))
