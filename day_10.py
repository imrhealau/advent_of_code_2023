from helper import Day

# class MazeSolver:
#     def __init__(self,maze):
#         self.maze = maze
#         self.route = []
#         self.checked = []
#         self.pipe = {
#             # a:b -> from a you can get to b
#             'north':{'|':['F','|'],'F':['-','7'],},
#             'south':{'|':['L','|'],'L':['-','J'],},
#             'west':{'-':['-','F'],'F':['|','L'],},
#             'east':{'-':['-','7'],'7':['|','J']}
#         }

#     def find_start(self):
#         for y in range(len(self.maze)):
#             for x in range(len(self.maze[0])):
#                 if self.maze[y][x]=='S':
#                     self.start = (y,x)
#         return self.start
                
#     def can_move_to(self, current_ele, dir, position:tuple):
#         print(position)
#         y,x = position
#         if 0 <= y < len(self.maze) and 0 <= x < len(self.maze) and \
#             self.maze[y][x] != '.' and self.maze[y][x] in self.pipe[dir][current_ele]:
#             return True
#         return False
    
#     def find_route(self, position:tuple):
#         y,x = position

#         if position in self.checked:
#             return False
#         self.checked.append(position)

#         if position == self.start and len(self.route)!=0:
#             return True
        
#         north = (position[0] - 1, position[1])
#         south = (position[0] + 1, position[1])
#         west = (position[0], position[1] - 1)
#         east = (position[0], position[1] + 1)
#         possible_next_position = [north, south, west, east]
#         for next_position in possible_next_position:
#             if self.can_move_to(self.maze[y][x],str(next_position),next_position):
#                 self.route.append(position)
#                 return True
#         self.route.pop()  # restore the route back to what it was before we executed this step. 
#         return False
        
#     def solve_maze(self):
#         if self.find_route(self.find_start()):
#             return self.route
#         return None

# def find_start(maze):
#     for y in range(len(maze)):
#         for x in range(len(maze[0])):
#             if maze[y][x]=='S':
#                 start = (y,x)
#     return start    

# def find_route(maze,start,move):
#     route = [start]
#     position = start
#     pipe = {
#         # a:b -> from a you can get to b
#         'north':{'|':['F','|'],'F':['-','7'],},
#         'south':{'|':['L','|'],'L':['-','J'],},
#         'west':{'-':['-','F'],'F':['|','L'],},
#         'east':{'-':['-','7'],'7':['|','J']}
#         }
#     while maze[position[0]][position[1]] != 'S':





def solution(data,part_two):  
    maze = data
    start = find_start(data)


    if part_two:
        return

    return mazesolver.solve_maze()




day = Day(10,solution)
day.test()
# day.solve()