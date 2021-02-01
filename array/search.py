#!/usr/bin/python

def search(ary, num):
    begin = 0
    end = len(ary) - 1

    while True:
        if begin > end:
            break
        mid = int((begin + end) / 2)
        print("begin: %d, end: %d, mid: %d" % (begin, end, mid))
        if num == ary[mid]:
            return mid
        elif num > ary[mid]:
            begin = mid + 1
        else:
            end = mid
    return -1

if __name__ == '__main__':
    found = 0
    ary = [1,2,4,6,8,10,24,25,36,48]
    for i in range(50):
        res = search(ary, i)
        if res > -1:
            found += 1
        print("index of {index}: {result}".format(index=i, result=res))

    print("len: %d, found: %d" % (len(ary), found))
    #print(search(ary, 25))
