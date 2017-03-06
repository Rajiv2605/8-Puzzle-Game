from queue import Queue
from queue import LifoQueue
from copy import deepcopy

class State:
    def __init__(self, m, n, initialState):
        self.m = m
        self.n = n
        self.initialState = initialState
        self.parent = False
    
    def childNodes(self, currentState):
        self.currentState = currentState
        #print("Unchanged")
        #print(self.currentState)
        children = []
        #nochangestate = currentState
        if currentState != None:
            for i in range(self.m):
                for j in range(self.n):
                    if self.currentState[i][j] == 0:
                        self.I, self.J = i, j
                        break
                #Row
                for i in [self.I-1, self.I+1]:
                    #print("i")
                    #print(i)
                    #temp2 = self.currentState
                    if(self.isExists(i, self.J, self.n)):
                        #print("i")
                        #print(i)
                        #print("TEMP")
                        #print(self.currentState)
                        #z = self.swap(I, J, i, J, temp2)
                        children.append(self.swap(self.I, self.J, i, self.J, self.currentState))
                #Column
                for j in [self.J-1, self.J+1]:
                    #temp2 = self.currentState
                    if(self.isExists(self.I, j, self.n)):
                        #print(I)
                        #print(J)
                        #print("j")
                        #print(j)
                        #print("TEMP")
                        #print(self.currentState)
                        #z = self.swap(I, J, I, j, temp2)
                        children.append(self.swap(self.I, self.J, self.I, j, self.currentState))
                #print("found")
                return children
   
    def findDir(self, goal):
#        i=0
        print("Printing backtrackingX...")
        print(self.backtracking_x)
        print("Printing backtrackingY...")
        print(self.backtracking_y)
        x2, y2 = 0, 0
        x1, y1 = self.backtracking_x[x2][y2], self.backtracking_y[x2][y2]
        while x1>=0 and y1>=0:
#            i+=1
#            print("x1")
#            print(x1)
#            print("y1")
#            print(y1)
#            print("x2")
#            print(x2)
#            print("y2")
#            print(y2)
            if x1>x2:
                print("UP")
            if x2>x1:
                print("DOWN")
            if y1>y2:
                print("LEFT")
            if y2>y1:
                print("RIGHT")
            x2=deepcopy(x1)
            y2=deepcopy(y1)
            x1, y1 = deepcopy(self.backtracking_x[x2][y2]), deepcopy(self.backtracking_y[x2][y2])
        
    def swap(self, x, y, i, j, c):
#        d=c
#        print("Before swap")
#        print(c)
#        print("Element1")
#        print(d[i][j])
#        print("Element2")
#        print(d[x][y])
#        print("X")
#        print(x)
#        print("Y")
#        print(y)
        d = deepcopy(c)
        temp=0
        temp = d[x][y]
        d[x][y] = d[i][j]
        d[i][j] = temp
        #d.parent=c
        #print("d")
        #print(d==c)
        #print("c")
        #print(c)
#        print("After swap")
#        print("Element1")
#        print(c[i][j])
#        print("Element2")
#        print(c[x][y])
        if d not in self.visited:
            self.backtracking_x[i][j] = x
            self.backtracking_y[i][j] = y
            return d
        
    def isExists(self, x, y, n):
        return (x>=0) and (y>=0) and (x<n) and (y<n)
    def bfs(self):
        #reached=False
        #b=0
        self.backtracking_x = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.backtracking_y = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.visited = []
        goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        frontier = Queue()
        frontier.put(self.initialState)
        while(1):
            #print("Searching")
            #print(reached)
            currentNode = frontier.get()
            print("Printing current node..")
            print(currentNode)
            print("Visited")
            print(self.visited)
            if currentNode == goal:
                print("Goal reached")
                self.visited.append(currentNode)
                print(self.visited)
                print("Printing directions...")
                self.findDir(goal)
                break
            elif currentNode not in self.visited and currentNode!=None:
                #print("Inside")
                self.visited.append(currentNode)
                l = self.childNodes(currentNode)
                #print("Printing l")
                #print(l)
                for i in range(len(l)):
                    frontier.put(l[i])
            else:
                pass
#    def dfs(self):
#        #reached=False
#        #b=0
#        visited = []
#        goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
#        frontier = LifoQueue()
#        frontier.put(self.initialState)
#        while(1):
#            #print("Searching")
#            #print(reached)
#            currentNode = frontier.get()
#            print("Printing current node..")
#            print(currentNode)
#            print("Visited")
#            print(visited)
#            if currentNode == goal:
#                print("Goal reached")
#                visited.append(currentNode)
#                print(visited)
#                break
#            elif currentNode not in visited:
#                #print("Inside")
#                visited.append(currentNode)
#                l = self.childNodes(currentNode)
#                #print("Printing l")
#                #print(l)
#                for i in range(len(l)):
#                    frontier.put(l[i])
#            else:
#                pass
#                #if len(visited)>100:
#                #    print("No solution")
#                #    break        
if __name__ == "__main__":
    initial = input("Enter: ")
    a = initial.split()
    l = []
    main = []
    m, n = int(len(a)**(0.5)), int(len(a)**(0.5))
    for i in range(m):
        for j in range(3*i, 3*(i+1)):
            l.append(int(a[j]))
        main.append(l)
        l = []
    initialState = State(m, n, main)
    initialState.bfs()