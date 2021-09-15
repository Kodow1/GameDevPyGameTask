#Mazing trial

import random

class Edge():
  def __init__(self,x,y,direction):
    self.x = x 
    self.y = y
    self.direction = direction
    
    
class Cell():
    def __init__(self,name,x,y):
        self.tree = ''
        self.name = name
        self.left = True
        self.right = True
        self.up = True
        self.down = True
        self.x = x
        self.y = y
        self.adjacent = {}
        self.shared_walls = []
class Tree():
    def __init__(self,name):
        self.name = name
        self.branches = []
        pass
def generate_maze(width,height):
    maze = [
    #  x  0   1   2   3   4   5   6   7   8   9   10  11  12  13    y
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #0
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #1
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #2
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #3
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #4
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #5
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #6
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #7
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #8
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."]] #9
    section_maze = [
    #  x  0   1   2   3   4   5   6   7   8   9   10  11  12  13    y
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #0
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #1
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #2
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #3
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #4
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #5
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #6
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #7
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."], #8
        [".",".",".",".",".",".",".",".",".",".",".",".",".","."]] #9
    #cell creation
    cell_list = []
    for x in range(width):
        for y in range(height):
            name = str(x)+str(y)
            cell_list.append(Cell(name,x,y))
    #adding adjacent
    for cell in cell_list:
        if cell.x != 0: #not on left edge
            cell.adjacent["left"]= int(cell.name)-10
            cell.shared_walls.append("left")
        if cell.x != 13: #not on right edge
            cell.adjacent["right"]= int(cell.name)+10
            cell.shared_walls.append("right")
        if cell.y != 0: #not on top edge
            cell.adjacent["up"] = int(cell.name)-1
            cell.shared_walls.append("up")
        if cell.y != 9: #not on bottom edge
            cell.adjacent["down"] = int(cell.name)+1
            cell.shared_walls.append("down")
            
    #cell editing
    complete = False
    counter = 0
    tree_list = []
    not_done_cells = []
    for cell in cell_list:
        cell.tree = Tree(int(cell.name))
        tree_list.append(cell.tree)
        cell.tree.branches.append(int(cell.name))
    for cell in cell_list:
        not_done_cells.append(cell.name)
    print ("wtf")
    while not complete:
    #while len(not_done_cells) > 0:
    #while counter < 10:
        counter += 1
        print(len(not_done_cells),"/140")
        num_cell = random.randint(0,len(not_done_cells)-1)#random cell
        cell = cell_list[int(not_done_cells[num_cell])] 
        #print(cell.tree.name)
        if len(cell.shared_walls) != 0:
            if len(cell.shared_walls) != 1:
                num = random.randint(0,len(cell.shared_walls)-1)
            else:
                num = 0
            wall = cell.shared_walls[num] #up,down,left or right
            adj_cell = cell_list[int(cell.adjacent[wall])]
            if adj_cell.name not in cell.tree.branches:
                #removing walls
                cell.shared_walls.remove(wall)
                if wall == "up":
                    cell.up = False
                    adj_cell.down = False
                elif wall == "down":
                    cell.down = False
                    adj_cell.down = False
                elif wall == "left":
                    cell.left = False
                    adj_cell.right = False
                elif wall == "right":
                    cell.right = False
                    adj_cell.left = False
                #adding all of the names in adj_cell.tree into cell.tree
                for o_cell_name in adj_cell.tree.branches:
                    if o_cell_name != adj_cell.name:
                        cell.tree.branches.append(int(o_cell_name))
                        o_cell.tree = cell.tree
                cell.tree.branches.append(int(adj_cell.name))
                tree_list.remove(adj_cell.tree)
                adj_cell.tree = cell.tree
                #replacing all the old trees in everything cell.tree has absorbed
                for o_cell_name in cell.tree.branches:
                    o_cell = cell_list[int(o_cell_name)]
                    o_cell.tree = cell.tree
            for cell in cell_list:
                section_maze[cell.y][cell.x] = cell.tree.name
            print("maze:")
            for line in section_maze:
                print(line)
            print("trees")
            for tree in tree_list:
                print (tree.name,tree.branches)
            #breaking out of the loop
            complete = True
            for o_cell in cell_list:
                if o_cell.tree != cell.tree:
                    complete = False
            
        #removing cell for cell_list if finished
        for adj_cell in cell.adjacent.values():
            test = int(adj_cell)
            adj_cell = cell_list[test]
            if cell.tree != adj_cell.tree:
                cell_finished = False
        if cell_finished == True:
            not_done_cells.remove(cell.name)
            print("removed")
    #editing map.
    for cell in cell_list:
        section_maze[cell.y][cell.x] = cell.tree.name
        if cell.up == True and cell.left == True:
            maze[cell.y][cell.x] = "T"
        elif cell.up == True:
            maze[cell.y][cell.x] = "-"
        elif cell.left == True:
            maze[cell.y][cell.x] = "l"
        else:
            maze[cell.y][cell.x] = "."
    for line in maze:
        print(line)
    for line in section_maze:
        print(line)
    return maze
    