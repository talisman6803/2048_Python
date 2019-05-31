# 1-Dimension board(Original)
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

# 2-Dimension board
# 0  1  2  3
# 4  5  6  7
# 8  9  10 11
# 12 13 14 15

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
