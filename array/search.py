#!/usr/bin/python

def binary_search(ary, num):
    begin = 0
    end = len(ary)

    while True:
        if begin >= end:
            break
        mid = int((begin + end) / 2)
        #print("begin: %d, end: %d, mid: %d" % (begin, end, mid))
        if num == ary[mid]:
            return mid
        elif num > ary[mid]:
            begin = mid + 1
        else:
            end = mid
    return -1

def rotated_sort_array_binary_search(ary, num):
    begin = 0
    end = len(ary)

    while True:
        if begin >= end:
            break
        mid = int((begin + end) / 2)
        if num == ary[mid]:
            return mid
        if num > ary[mid]:
            if num == ary[end-1]:
                return end-1
            elif num < ary[end-1]:
                begin = mid + 1
            else:
                end = mid
        else:
            if num == ary[begin]:
                return begin
            elif num > ary[begin]:
                end = mid
            else:
                begin = mid + 1
    return -1

def rotate_array(ary, count):
    if count <= 0 or count >= len(ary):
        return ary
    return ary[count:] + ary[:count]

if __name__ == '__main__':
    ary = [1,2,4,6,8,10,24,25,36,48]

    # binary search testcase in sort array
    found = 0
    for i in range(50):
        res = binary_search(ary, i)
        if res > -1:
            found += 1
        #print("index of {index}: {result}".format(index=i, result=res))
    print("len: %d, found: %d" % (len(ary), found))

    # binary search in rotated sort array testcase
    for count in range(1, len(ary) - 1):
        print(rotate_array(ary, count))
        fount = 0
        for i in range(50):
            res = rotated_sort_array_binary_search(ary, i)
            if res > -1:
                fount += 1
        print("%d, len: %d, found: %d" % (count, len(ary), found))


