
class Maze():
    def __init__(self,maze_list):
        self.maze_list = maze_list
        self.currentx = 0
        self.stepx = 0

    def gomaze(self):

        # decide right direction
        #self.decide_dir()
        if self.maze_list[self.currentx] == 0:
            # If failed, go back one step
            self.currentx -= 1
            print('stopped at :', self.currentx)
            return False, self.stepx

        # Reach the terminal
        elif self.maze_list[self.currentx] == 2:
            return True, self.stepx

        # Be able to continue
        elif self.maze_list[self.currentx] == 1:
            self.stepx += 1
            self.currentx += 1
            return self.gomaze()  
        else:
            return False, 'wrong maze!'

if __name__ == '__main__':
    maze_list1 = [1,1,0,1,2,0] 
    maze1 = Maze(maze_list1)
    ret,steps = maze1.gomaze()
    print(steps,ret)
