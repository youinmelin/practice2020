import random

class Maze():
    def __init__(self,maze_list):
        self.maze_list = maze_list
        self.currentx = 1
        self.currenty = 1
        self.stepx = 0

    def go_ahead(self):
        # print(f'x={x},y={y},{direction}')
        dir_list = [[0,1,'down'],[1,0,'right'],[0,-1,'up'],[-1,0,'left']]
        y,x,direction = dir_list[random.randint(0,3)]
        # dir_dict = {'down':[0,1],'right':[1,0],'up':[0,-1],'left':[-1,0]}
        # direction = input('input a direction:')
        # y,x = dir_dict[direction]
        print(direction)
        self.currentx += x
        self.currenty += y
        if self.maze_list[self.currentx][self.currenty] == 0:
            # If failed, go back one step
            self.currentx -= x
            self.currenty -= y
            self.stepx -= 1
            print('back to :', self.currenty, self.currentx)
            #return False, self.stepx
            self.go_ahead()  

        # Reach the terminal
        elif self.maze_list[self.currentx][self.currenty] == 2:
            print('stopped at :', self.currenty, self.currentx)
            print('steps is :', self.stepx)
            return True, self.stepx

        # Be able to continue
        elif self.maze_list[self.currentx][self.currenty] == 1:
            self.stepx += 1
            print('try :', self.currenty, self.currentx)
            self.go_ahead()  
        else:
            return 'wrong maze!', self.stepx


if __name__ == '__main__':
    maze_list1 = [
                  [0,0,0,0,0,0,0],
                  [0,1,1,1,1,1,0],
                  [0,0,0,1,0,0,0],
                  [0,0,0,1,1,1,0],
                  [0,0,0,1,1,1,0],
                  [0,0,0,1,1,1,0],
                  [0,0,0,1,1,1,0],
                  [0,0,0,1,1,1,0],
                  [0,0,0,1,1,1,0],
                  [0,0,0,0,1,1,0],
                  [0,1,1,1,0,1,0],
                  [0,1,1,0,1,1,0],
                  [0,1,1,1,1,2,0],
                  [0,0,0,0,0,0,0]]
    # print(maze_list1)
    maze1 = Maze(maze_list1)
    maze1.go_ahead()
