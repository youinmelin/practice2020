from random import choice 
import sys
sys.setrecursionlimit(10000)  # set the maximum depth as 10000
class Maze():
    def __init__(self,maze_list):
        self.maze_list = maze_list
        self.currentx = 1
        self.currenty = 1
        self.stepx = 0

    def go_ahead(self,dir_num=0):
        # print(f'x={x},y={y},{direction}')
        if dir_num > 3:
            dir_num = 0
        dir_list = [[0,1,'down'],[1,0,'right'],[0,-1,'up'],[-1,0,'left']]
        # y,x,direction = dir_list[random.randint(0,3)]
        y,x,direction = dir_list[dir_num]
        print(direction)
        self.currentx += x
        self.currenty += y
        self.stepx += 1
        if self.maze_list[self.currentx][self.currenty] == 0:
            # If failed, go back one step
            self.currentx -= x
            self.currenty -= y
            if self.stepx > 0:
                self.stepx -= 1
            print('back to :', self.currenty, self.currentx)
            # if failed, change a direction
            self.go_ahead(dir_num+1)  

        # Be able to continue
        elif self.maze_list[self.currentx][self.currenty] == 1:
            print('try :', self.currenty, self.currentx, 'step :', self.stepx)
            random_list = [0,1,2,3]
            dir_opp_num = (dir_num + 2) % 4
            #print(dir_num,dir_opp_num)
            random_list.remove(dir_num)
            # self.go_ahead(choice(random_list))  
            self.go_ahead(choice([0,1,2,3]))  

        # Reach the terminal
        elif self.maze_list[self.currentx][self.currenty] == 2:
            print('stopped at :', self.currenty, self.currentx)
            print('steps is :', self.stepx)
            return True, self.stepx

        else:
            return 'wrong maze!', self.stepx

if __name__ == '__main__':
    maze_list1 = [
                  [0,0,0,0,0,0,0],
                  [0,1,1,1,0,0,0],
                  [0,0,0,1,0,0,0],
                  [0,0,0,1,0,0,0],
                  [0,0,0,1,0,0,0],
                  [0,0,0,1,0,0,0],
                  [0,0,0,1,1,1,0],
                  [0,0,0,0,0,1,0],
                  [0,1,1,1,0,1,0],
                  [0,1,1,0,0,1,0],
                  [0,1,1,0,1,2,0],
                  [0,0,0,0,0,0,0]]
    # print(maze_list1) 
    maze1 = Maze(maze_list1)
    maze1.go_ahead()
