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

def main():
    print("Welcome To 2048")
    print("Push W/A/S/D to Play.")
    bd = new_game()
    bd = board_add(bd)
    bd = board_add(bd)
    print_board(bd)
