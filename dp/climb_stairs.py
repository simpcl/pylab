#!/usr/bin/python

max_step_num = 3

def climb_stairs(stairs_num):
    if stairs_num <= 0:
        return 0
    elif stairs_num == 1:
        return 1
    elif stairs_num == 2:
        return 2
    elif stairs_num == 3:
        return 4

    return climb_stairs(stairs_num - 1) + climb_stairs(stairs_num - 2) + climb_stairs(stairs_num - 3)

if __name__ == '__main__':
    for i in [3,4,5,10,25]:
        print(i, climb_stairs(i))
