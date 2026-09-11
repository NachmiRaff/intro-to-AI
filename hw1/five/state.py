'''
The state is a list of 2 items: the board, the path
The target for 8-puzzle is: (zero is the hole)
012
345
678
'''
import random
import math

#returns a random board nXn
def create(n):
    s=list(range(n*n))      # s is the board itself. a vector that represent a matrix. s=[0,1,2....n^2-1]
    m="<>v^"                # m is "<>v^" - for every possible move (left, right, down, up)
    for i in range(n**3):  # makes n^3 random moves to mix the tiles
        if_legal(s,m[random.randrange(4)])
    return [s,""]           # at the beginning "" is an empty path, later on path
                            # contains the path that leads from the initial state to the state

def get_next(x):            # returns a list of the children states of x
    ns=[]                   # the next state list
    for i in "<>v^":
        s=x[0][:]           # [:] - copies the board in x[0]
        if_legal(s,i)       # try to move in direction i
        # checks if the move was legal and...
        if s.index(0)!=x[0].index(0) and \
           (x[1]=="" or x[1][-1]!="><^v"["<>v^".index(i)]): # check if it's the first move or it's a reverse move
            ns.append([s,x[1]+i])   # appends the new state to ns
    return ns


def path_len(x):
    return len(x[1])

def is_target(x):
    n=len(x[0])                     # the size of the board
    return x[0]==list(range(n))     # list(range(n)) is the target state

#############################
def if_legal(x,m):                  # gets a board and a move and makes the move if it's legal
    n=int(math.sqrt(len(x)))        # the size of the board is nXn
    z=x.index(0)                    # z is the place of the empty tile (0)
    if z%n>0 and m=="<":            # checks if the empty tile is not in the first col and the move is to the left
        x[z]=x[z-1]                 # swap x[z] and x[z-1]...
        x[z-1]=0                    # ...and move the empty tile to the left
    elif z%n<n-1 and m==">":        # check if the empty tile is not in the n's col and the move is to the right
        x[z]=x[z+1]
        x[z+1]=0
    elif z>=n and m=="^":           # check if the empty tile is not in the first row and the move is up
        x[z]=x[z-n]
        x[z-n]=0
    elif z<n*n-n and m=="v":        # check if the empty tile is not in the n's row and the move is down
        x[z]=x[z+n]
        x[z+n]=0

# This is your HW
def hdistance0(s):                   # the heuristic value of s -- uniform cost
    return 0

def hdistance1(s):
    num = 0
    board = s[0]
    for i in range(len(board)):
        if board[i]!=i and board[i]!=0:
            num+=1
    return num

def hdistance2(s):
    num = 0
    board = s[0]
    n = int(math.sqrt(len(board)))
    for i in range(len(board)):
        if board[i]!=0:
            cur_row = i // n
            cur_col = i % n

            target_row = board[i] // n
            target_col = board[i] % n

            num += abs(cur_row - target_row)
            num += abs(cur_col - target_col)
    return num

def weighted(s):
    return 4*hdistance2(s)+hdistance1(s)

def hdistance3_blog(s):
    board = s[0]
    n = int(math.sqrt(len(board)))

    count = 0
    for i in range(n):
        for j in range(n):
            cur = board[n*i+j]
            if cur//n!=i or cur==0:
                continue
            for k in range(j+1,n):
                new = board[n*i+k]
                if new//n==i and cur>new and new!=0:
                    count+=2

    for i in range(n):
        for j in range(n):
            cur = board[i+j*n]
            if cur%n!=i or cur==0:
                continue
            for k in range(j+1,n):
                new = board[i+k*n]
                if new%n==i and cur>new and new!=0:
                    count+=2
    return count + hdistance2(s)
    
def hdistance3(s):
    board = s[0]
    n = int(math.sqrt(len(board)))

    count = 0
    for i in range(n):
        removed = set()
        nums = [1]
        while(any(nums)):
            nums = [0]*n
            for j in range(n):
                cur = board[n*i+j]
                if cur//n!=i or cur==0 or j in removed:
                    continue
                for k in range(j+1,n):
                    new = board[n*i+k]
                    if new//n==i and cur>new and new!=0 and k not in removed:
                        nums[j]+=1
                        nums[k]+=1
            loc = nums.index(max(nums))
            if nums[loc] != 0:
                count+=2
                removed.add(loc)

        removed = set()
        nums = [1]
        while(any(nums)):
            nums = [0]*n
            for j in range(n):
                cur = board[i+j*n]
                if cur%n!=i or cur==0 or j in removed:
                    continue
                for k in range(j+1,n):
                    new = board[i+k*n]
                    if new%n==i and cur>new and new!=0 and k not in removed:
                        nums[j]+=1
                        nums[k]+=1
            loc = nums.index(max(nums))
            if nums[loc] != 0:
                count+=2
                removed.add(loc)
    return count + hdistance2(s)