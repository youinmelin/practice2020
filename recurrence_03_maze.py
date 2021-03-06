from random import choice 
import sys
sys.setrecursionlimit(3000)  # set the maximum depth as 3000

# 0: wall, 1:road, 2:terminal, 3:wrong road, 4:passed road

class Maze():
    def __init__(self,maze_list):
        self.maze_list = maze_list
        self.currentx = 1
        self.currenty = 1
        self.stepx = 0
        self.wrong_num = 0

    def go_ahead(self,dir_num=0):
        # print(f'x={x},y={y},{direction}')
        if dir_num > 3:
            dir_num = 0
        #dir_list = [[1,0,'right'],[0,1,'down'],[-1,0,'left'],[0,-1,'up']]
        dir_list = [[1,0,'down'],[0,1,'right'],[-1,0,'up'],[0,-1,'left']]
        #dir_list = [[0,1,'down'],[1,0,'right'],[0,-1,'up'],[-1,0,'left']]
        # y,x,direction = dir_list[random.randint(0,3)]
        x,y,direction = dir_list[dir_num]
        print(y,x,direction,end='  ')
        self.currentx += x
        self.currenty += y
        self.stepx += 1
        print('try:', self.currenty, self.currentx, 'step :', self.stepx)
        # wrong_num : count continuous wrong steps
        block = self.maze_list[self.currentx][self.currenty]
        if  block == 0 or block == 3 or block == 4:
            # If failed, go back one step
            self.currentx -= x
            self.currenty -= y
            self.stepx -= 1
            self.wrong_num += 1
            print('----wrong---- ',self.wrong_num)
            # if continuous wrong steps is 3,then set this block is 0
            if self.wrong_num == 4:
                self.maze_list[self.currentx][self.currenty] = 1
                self.wrong_num = 0
            # if self.wrong_num == 3:
            #    self.maze_list[self.currentx][self.currenty] = 3
            print('back to :', self.currenty, self.currentx)
            print(f'current x,y = {self.currentx},{self.currenty} ')
            # if failed, change a direction
            self.go_ahead(dir_num+1)  

        # Be able to continue
        elif self.maze_list[self.currentx][self.currenty] == 1:
            self.wrong_num = 0
            self.passedx = self.currentx - x
            self.passedy = self.currenty - y
            self.maze_list[self.passedx][self.passedy] = 4
            print(f'{self.passedx},{self.passedy} = 4')
            print(f'current x,y = {self.currentx},{self.currenty} ')
            self.go_ahead(choice([0,1,2,3]))  

        # Reach the terminal
        elif self.maze_list[self.currentx][self.currenty] == 2:
            print('stopped at :', self.currenty, self.currentx)
            print('steps is :', self.stepx)
            return True, self.stepx

        else:
            return 'wrong maze!', self.stepx

if __name__ == '__main__':
    maze_list1 = [[0,0,0,0,0,0,0],
                  [0,1,1,1,1,2,0],
                  [0,0,0,0,0,0,0]]
    maze_list2 = [[0,0,0],
                  [0,1,0],
                  [0,1,0],
                  [0,1,0],
                  [0,1,0],
                  [0,2,0],
                  [0,0,0]]
    maze_list3 = [[0,0,0,0,0,0,0],
                  [0,1,1,1,1,0,0],
                  [0,0,1,1,1,2,0],
                  [0,0,0,0,0,0,0]]
    # print(maze_list1) 
    maze1 = Maze(maze_list3)
    maze1.go_ahead()
    for i in maze1.maze_list:
        print(i)
