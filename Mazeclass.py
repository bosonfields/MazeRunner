import numpy as np
import random
import matplotlib.cm as cm
from matplotlib import pyplot as plt


#Generalize a maze with dimension and probability
class Maze:
    def __init__(self, num, p = 0):
        self.dim = num
        self.M = np.random.rand(self.dim, self.dim)
        blank = self.M >= p
        blocked = self.M<p
        self.M[blank] = 1
        self.M[blocked] = 0
        self.M[0,0]=1
        self.M[self.dim - 1, self.dim - 1] = 1

    def readMaze(self, m):
        self.dim = len(m)
        self.M = m

    #Return the available
    def get_available_neighbors(self, node):
        rows, cols = node
        adj = [(rows - 1, cols), (rows + 1, cols), (rows, cols - 1), (rows, cols + 1)] #left, right, down, up
        choice = []
        if adj[0][0] >= 0 and self.M[adj[0]]==1:
            choice.append(adj[0])
        if adj[1][0] <self.dim and self.M[adj[1]]==1:
            choice.append(adj[1])
        if adj[2][1] >= 0 and self.M[adj[2]]==1:
            choice.append(adj[2])
        if adj[3][1] <self.dim and self.M[adj[3]]==1:
            choice.append(adj[3])
        return choice

    def Euclidean_distance(self, node):
        row, col = node
        distance = np.sqrt((self.dim - row) ** 2 + (self.dim - col) ** 2)
        return distance
    def get_nearest_neighbors(self, node):
        rows, cols = node
        adj = [(rows - 1, cols), (rows, cols - 1), (rows + 1, cols),  (rows, cols + 1) ]  # left, up, right, down
        choice = []
        if adj[0][0] >= 0 and self.M[adj[0]] == 1:
            choice.append(adj[0])
        if adj[1][1] >= 0 and self.M[adj[1]]== 1:
            choice.append(adj[1])
        if adj[2][0] < self.dim and self.M[adj[2]] == 1:
            choice.append(adj[2])
        if adj[3][1] < self.dim and self.M[adj[3]] == 1:
            choice.append(adj[3])
        return choice


    def show_figure(self, route=[(0,0)]):
        if self.dim<=75:
            self.showMaze_route_grid(route)
        else:
            self.showMaze_route(route)

    # Generalize a image with some grids
    def showMaze_route_grid(self, route):
        image = np.zeros((self.dim * 10 + 1, self.dim * 10 + 1), dtype = np.uint8)
        for row in range(self.dim):
            for col in range(self.dim):
                for i in range(10 * row+1, 10* row +10):
                    if (row, col) in route and self.M[row, col] ==0:
                        print("Route conflicted with blocks")
                    elif (row, col) in route:
                        image[i, range(10 * col+1, 10 * col + 10)] = np.uint8(128)
                    elif self.M[row,col]==0:
                        image[i, range(10 * col+1, 10 * col + 10)] = np.uint8(0)
                    else:
                        image[i, range(10 * col + 1, 10 * col + 10)] = np.uint8(225)
        plt.imshow(image, cmap=cm.Greys_r, vmin=0, vmax=255, interpolation='none')
        plt.show()

    def showMaze_route(self,route):
        image = self.M.astype(np.uint8).copy()
        image[image==np.uint8(1)] = np.uint8(255)
        for row, col in route:
            image[row, col]=np.uint8(128)
        plt.imshow(image, cmap=cm.Greys_r, vmin=0, vmax=255, interpolation='none')
        plt.show()

    def random_change_pairs(self):
        blank = np.random.randint(self.dim, size = 2)
        block = np.random.randint(self.dim, size = 2)
        self.M[block] = 0
        self.M[blank] = 1
        self.M[0,0] = 1
        self.M[self.dim - 1, self.dim - 1] = 1
        return ((block[0], block[1]), (blank[0],blank[1]))








