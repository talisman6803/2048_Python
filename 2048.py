import random
import sys

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
    if random.random()+0.85>=1:
        lt[temp] = 2
    else :
        lt[temp] = 4
    return lt

def print_board(lt):
    print("|---------------------------|")
    for i in range(len(lt)):
        print("|", end='')
        print("", lt[i], end='')
        for j in range(5-len(str(lt[i]))):
            print(" ", end='')
        if i%4 == 3:
            print("|")
            print("|------+------+------+------|")


def key_in(lt):
    print("Distinguish only W/A/S/D/X")
    x = input()
    while True:
        if x == 'w':
            lt = mu(lt)
            break
        elif x == 'a':
            lt = ml(lt)
            break
        elif x == 's':
            lt = md(lt)
            break
        elif x == 'd':
            lt = mr(lt)
            break
        elif x == 'x':
            print("GAME EXIT")
            sys.exit()
        else:
            print("INCORRECT INPUT!")
            x = input()
    return lt

def merge(oneline):
    for i in range(3):
        if oneline[i] != 0:
            for j in range(3-i):
                if oneline[i] == oneline[j+i+1]:
                    oneline[i] = oneline[i] * 2
                    oneline[i+j+1] = 0
                    break
                elif oneline[j+i+1] == 0:
                    continue
                else:
                    break
        else:
            continue
    idx = 0
    cnt = 0
    while idx < 4:
        if oneline[idx] == 0 and cnt != 3:
            del oneline[idx]
            oneline.append(0)
            idx = 0
            cnt += 1
        else :
            idx += 1
    return oneline

def mu(lt):
    for i in range(4):
        lt[i],lt[4+i],lt[8+i],lt[12+i] = merge([lt[i],lt[4+i],lt[8+i],lt[12+i]])
    return lt

def md(lt):
    for i in range(4):
        lt[12+i],lt[8+i],lt[4+i],lt[i] = merge([lt[12+i],lt[8+i],lt[4+i],lt[i]])
    return lt

def ml(lt):
    for i in range(4):
        lt[i*4],lt[1+i*4],lt[2+i*4],lt[3+i*4] = merge([lt[i*4],lt[1+i*4],lt[2+i*4],lt[3+i*4]])
    return lt

def mr(lt):
    for i in range(4):
        lt[3+i*4],lt[2+i*4],lt[1+i*4],lt[i*4] = merge([lt[3+i*4],lt[2+i*4],lt[1+i*4],lt[i*4]])
    return lt

def gameover(bd):
    for i in range(15):
        if bd[i] == bd[i+1]:
            return False
    for i in range(4):
        if bd[i] == bd[i+4]:
            return False
        if bd[i+8] == bd[i+12]:
            return False
    return True


def main():
    print("Welcome To 2048")
    print("Push W/A/S/D to Play(exit:x).")
    bd = new_game()
    bd = board_add(bd)
    bd = board_add(bd)
    print_board(bd)
    cnt = 0
    t = 0
    while cnt == 0:
        try:
            print(t, "moves")
            key_in(bd)
            bd = board_add(bd)
            print_board(bd)
            t += 1
            for i in range(len(bd)):
                if bd[i] == 2048:
                    print("You've got 2048 on your board through", t,"times of move.")
                    cnt += 1
                    break

        except ValueError:
            if gameover(bd):
                print("GAME OVER!")
                sys.exit()
            print_board(bd)
            print("retry!")



main()
