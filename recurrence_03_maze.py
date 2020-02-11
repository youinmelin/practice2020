
class Maze():
    def __init__(self,maze_list):
        self.maze_list = maze_list
        self.currentx = 1
        self.currenty = 1
        self.stepx = 0

    def gomaze(self):

        # decide right direction
        for x,y,direction in [[0,1,'down'],[1,0,'right'],[0,-1,'up'],[-1,0,'left']]:
            result,step_times = self.go_ahead(x,y,direction)    
            if result == False:
                continue
            else:
                return result,step_times

    def go_ahead(self,x,y,direction):
        print(f'x={x},y={y},{direction}')
        if self.maze_list[self.currentx][self.currenty] == 0:
            # If failed, go back one step
            self.currentx -= x
            self.currenty -= y
            self.stepx -= 1
            print('back to :', self.currenty, self.currentx)
            return False, self.stepx

        # Reach the terminal
        elif self.maze_list[self.currentx][self.currenty] == 2:
            print('stopped at :', self.currenty, self.currentx)
            return True, self.stepx

        # Be able to continue
        elif self.maze_list[self.currentx][self.currenty] == 1:
            self.stepx += 1
            self.currentx += x 
            self.currenty += y
            print('try :', self.currenty, self.currentx)
            return self.gomaze()  
        else:
            return 'wrong maze!', self.stepx


if __name__ == '__main__':
    maze_list1 = [
                  [0,0,0,0,0,0,0],
                  [0,1,1,1,1,1,0],
                  [0,0,0,0,1,1,0],
                  [0,0,0,0,1,1,0],
                  [0,0,0,0,1,1,0],
                  [0,0,0,0,1,1,0],
                  [0,0,0,0,1,1,0],
                  [0,1,1,1,0,1,0],
                  [0,1,1,0,1,1,0],
                  [0,1,1,1,2,0,0],
                  [0,0,0,0,0,0,0]]
    maze1 = Maze(maze_list1)
    ret,steps = maze1.gomaze()
    print(steps,ret)
