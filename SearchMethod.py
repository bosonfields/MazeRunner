import numpy as np
from Mazeclass import Maze
import sys
import heapq
sys.setrecursionlimit(1000000)

#Search method only with Euclidean priority
def A_star_heuristic_only(node, maze):
    path = []
    parent = {node: None}
    fringe = []
    heapq.heapify(fringe)
    heapq.heappush(fringe, (Euclidean_distance(node, maze), node))
    while fringe and not path:
        currentNode = heapq.heappop(fringe)[1]
        for choice in maze.get_available_neighbors(currentNode):
            if choice not in parent:
                parent[choice] = currentNode
                if choice == (maze.dim - 1, maze.dim - 1):
                    temp = choice
                    while temp:
                        path.insert(0, temp)
                        temp = parent[temp]
                heapq.heappush(fringe, (Euclidean_distance(choice, maze), choice))
    history = list(parent.keys())
    return path, history


#DFS function with weighted neighbors
def DFS_default(node, maze):
    path=[]
    parent = {node: None}
    fringe = [node]
    currentNode = node
    Max_path = maze.dim *maze.dim
    while fringe and not path:
        for choice in maze.get_available_neighbors(currentNode):
            if choice not in parent:
                parent[choice] = currentNode
                fringe.append(choice)
                if choice == (maze.dim - 1, maze.dim - 1):
                    temp = choice
                    while temp:
                        path.insert(0, temp)
                        temp = parent[temp]
        currentNode = fringe.pop()
    history = list(parent.keys())
    return path, history

#DFS function with weighted neighbors
def DFS_oriented(node, maze):
    path=[]
    parent = {node: None}
    fringe = [node]
    currentNode = node
    Max_fringe = len(fringe)
    while fringe and not path:
        if Max_fringe<len(fringe):
            Max_fringe = len(fringe)
        for choice in maze.get_nearest_neighbors(currentNode):
            if choice not in parent:
                parent[choice] = currentNode
                fringe.append(choice)
                if choice == (maze.dim - 1, maze.dim - 1):
                    temp = choice
                    while temp:
                        path.insert(0, temp)
                        temp = parent[temp]
        currentNode = fringe.pop()
    history = list(parent.keys())
    return path, history, Max_fringe

#BFS function
def BFS(node, maze):
    i=1
    level = {node : 0}
    parent = {node: None}
    fringe = [node]
    path = []
    while fringe and not path:
        next = []
        for currentNode in fringe:
            for choice in maze.get_available_neighbors(currentNode):
                if choice not in level:
                    level[choice] = i
                    parent[choice] = currentNode
                    next.append(choice)
                    if choice == (maze.dim-1, maze.dim-1):
                        temp = choice
                        while temp:
                            path.insert(0, temp)
                            temp = parent[temp]
        fringe = next
        i+=1
    history = list(parent.keys())
    return path, history

#Different heuristic distances
def Euclidean_distance(node, maze):
    row, col = node
    distance = np.sqrt((maze.dim-row)**2+(maze.dim-col)**2)
    return distance

#Different A_star function
#A_star function with Euclidean heuristic
#A_star function with Manhattan heuristic
def A_star_Euclidean(node, maze):
    path = []
    level = {node : 0}
    parent = {node : None}
    fringe = []
    heapq.heapify(fringe)
    heapq.heappush(fringe, (Euclidean_distance(node, maze)+level[node], node))
    while fringe and not path:
        currentNode = heapq.heappop(fringe)[1]
        for choice in maze.get_available_neighbors(currentNode):
            if choice not in parent:
                parent[choice] = currentNode
                level[choice] = level[currentNode] + 1
                if choice == (maze.dim - 1, maze.dim - 1):
                    temp = choice
                    while temp:
                        path.insert(0, temp)
                        temp = parent[temp]
                heapq.heappush(fringe, (Euclidean_distance(choice, maze) + level[choice], choice))
    history = list(parent.keys())
    return path, history

def Manhattan_distance(node, maze):
    row, col = node
    distance = np.abs(maze.dim-row) + np.abs(maze.dim-col)
    return distance

def A_star_Manhattan(node, maze):
    path = []
    level = {node : 0}
    parent = {node : None}
    fringe = []
    heapq.heapify(fringe)
    heapq.heappush(fringe, (Manhattan_distance(node, maze)+level[node], node))
    Max_fringe = len(fringe)
    while fringe and not path:
        if len(fringe)>Max_fringe:
            Max_fringe =len(fringe)
        currentNode = heapq.heappop(fringe)[1]
        for choice in maze.get_available_neighbors(currentNode):
            if choice not in parent:
                parent[choice] = currentNode
                level[choice] = level[currentNode] + 1
                if choice == (maze.dim - 1, maze.dim - 1):
                    temp = choice
                    while temp:
                        path.insert(0, temp)
                        temp = parent[temp]
                heapq.heappush(fringe, (Manhattan_distance(choice, maze) + level[choice], choice))
    history = list(parent.keys())
    return path, history, Max_fringe

#Calculate the probability when maze has dim: n and wall_generate_probability of p
def get_solvability(num, p):
    begin = (0,0)
    sol_count = 0.0
    for i in range(100):
        test = Maze(num, p)
        path, history = A_star_heuristic_only(begin, test)
        if path:
            sol_count+=1.0
    return sol_count/100