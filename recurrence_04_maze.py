'''重写了代码，更好地利用了递归的功能
对于下一步走不通的情况，直接返回前一步的坐标,以及下一个方向。
能走通的话，继续走，但是迫不得已还是利用了随机方向，因为对于
折返的情况，如果方向写固定的话有可能会造成死循环
问题在于，并没有将路径作为递归的依据，应该实现一直走一条路，
当这条路判断为死胡同的话，再往后退
'''
import random

class Maze():
    def __init__(self,maze_list):
        self.maze_list = maze_list
        self.step = 0
        self.step_list = []
        self.current_row = 1
        self.current_col = 0

    def gomaze(self, row = 0, col = 1, dir_num = 0):

        # decide right direction
        dir_list = [[1,0,'down'],[-1,0,'up'],[0,1,'right'],[0,-1,'left']]
        r, c, direction = dir_list[dir_num]
        print(f'row={r},column={c},{direction}')
        self.current_row = row
        self.current_col = col
        self.current_row += r
        self.current_col += c
        self.step += 1
        current_value = self.maze_list[self.current_row][self.current_col]
        print(f'current_value = {current_value}')

        if current_value == 2:
            print (f'row is {self.current_row},col is {self.current_col} ,{self.step} steps finished')
            return True
        if current_value == 1:
            print (f'current: {self.current_row} , {self.current_col}')
            dir_num = random.randint(0,3)
            self.gomaze(self.current_row,self.current_col,dir_num)
        if current_value == 0:
            self.step -= 1
            print(f'back to {row},{col}')
            dir_next_num = ( dir_num + 3 ) % 4
            return self.gomaze(row,col,dir_next_num)

if __name__ == '__main__':
    maze_list1 = [
                  [0,0,0,0,0,0,0],
                  [0,1,1,1,1,0,0],
                  [0,1,1,1,1,1,0],
                  [0,1,1,1,1,1,0],
                  [0,0,1,0,1,1,0],
                  [0,0,1,0,1,1,0],
                  [0,1,1,2,1,1,0],
                  [0,0,0,0,0,0,0]]
    maze1 = Maze(maze_list1)
    maze1.gomaze()
