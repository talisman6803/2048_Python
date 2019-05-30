import random

def new_game():
    init_board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    return init_board

def chk_board(lt):
    chklist = []
    for i in range(len(lt)):
        if lt[i] == 0:
            chklist.append(i)
    return chklist

def board_add(lt):
    chk = chk_board(lt)
    temp = chk[random.randint(0,len(chk)-1)]
    if random.random()+0.5>=1:
        lt[temp] = 2
    else :
        lt[temp] = 4
    return lt

def print_board(lt):
    for i in range(4):
        print(lt[0+4*i],lt[1+4*i],lt[2+4*i],lt[3+4*i])

def key_in(lt):
    print("Distinguish only W/A/S/D")
    x = input()
    while True:
        if x == 'w':
            break
        elif x == 'a':
            break
        elif x == 's':
            break
        elif x == 'd':
            break
        else:
            print("INCORRECT INPUT!")
    return lt

# 1-Dimension board(Original)
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

# 2-Dimension board
# 0  1  2  3
# 4  5  6  7
# 8  9  10 11
# 12 13 14 15

def merge(oneline):
    for i in range(4):
        
    return one

def mu(lt):
    for i in range(4):
        lt[i],lt[4+i],lt[8+i],lt[12+i] = merge([lt[i],lt[4+i],lt[8+i],lt[12+i]])
    return lt

def md(lt):
    for i in range(4):
        merge([lt[
def main():
    print("Welcome To 2048")
    print("Push W/A/S/D to Play.")
    bd = new_game()
    bd = board_add(bd)
    bd = board_add(bd)
    print_board(bd)
    
