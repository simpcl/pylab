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

def P(n):
    if n == 0:
        return 1
    total = 1
    for i in xrange(n):
        n = i + 1
        total = total * n
    return total

def climb_stairs2(stairs_num):
    count = 0 
    result = 0

    X = stairs_num / 3
    X += 1
    for i in xrange(X):
        x = X - i - 1
        #print x, "===> ",
        Y = (stairs_num - x * 3) / 2
        Y += 1
        for j in xrange(Y):
            y = Y - j - 1
            Z = stairs_num - x * 3 - y * 2
            s = x + y + Z
            #print ("%d, %d, %d, %d\n" % (Z, y, x, P(s))),
            result += P(s) / (P(x) * P(y) * P(Z))
            count += 1

    #print "count:", count, "result:", result
    return result

if __name__ == '__main__':
    for i in [3,4,5,10,20]:
        print("%d => %d" % (i, climb_stairs(i)))
        print("%d => %d" % (i, climb_stairs2(i)))

