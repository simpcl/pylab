#!/usr/bin/python3

def two_sum(ary, target):
    d = {}
    for i in range(len(ary)):
        num = target - ary[i]
        if num < 0 or num >= len(ary):
            continue
        if num in d:
            print("(%d, %d) => (%d, %d)" % (i, d[num], ary[i], num))
        d[ary[i]] = i


if __name__ == '__main__':
    ary = [1,2,3,5,7,8,10,12,15,16,18,20,24,28]
    two_sum(ary, 22)   
