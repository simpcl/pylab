#!/usr/bin/python3

def find_single_number(ary):
    if ary[0] != ary[1]:
        return ary[0]

    prev = ary[0]
    flag = False

    for i in ary[1:]:

        if flag == True:
            if prev != i:
                return prev
            flag = False
        else:
            if prev != i:
                flag = True

        prev = i 

    if flag == True:
        return ary[len(ary)-1]

def find_single_number2(ary):
    begin = 0
    end = len(ary)
    mid = 0

    while True:
        if end - begin == 1:
            return ary[begin]

        mid = int((begin + end) / 2)

        #print ">>> begin: %d, end: %d, mid: %d" % (begin, end, mid)

        if (mid - begin) % 2 == 0:
            if ary[mid] == ary[mid + 1]:
                begin = mid + 2
            elif ary[mid] != ary[mid - 1]:
                return ary[mid]
            else:
                end = mid - 1
        else:
            if ary[mid] == ary[mid + 1]:
                end = mid
            elif ary[mid] != ary[mid - 1]:
                return ary[mid]
            else:
                begin = mid + 1

        #print "<<< begin: %d, end: %d" % (begin, end)

    return -1

if __name__ == '__main__':
    ary = [1,1,3,3,8,8,2,9,9,10,10]
    print("found: %d" % find_single_number(ary))
    print("found: %d" % find_single_number2(ary))
    ary = [1,1,2,8,8,9,9,10,10]
    print("found: %d" % find_single_number(ary))
    print("found: %d" % find_single_number2(ary))
    ary = [1,1,3,3,8,8,2,9,9,10,10,12,12,14,14]
    print("found: %d" % find_single_number(ary))
    print("found: %d" % find_single_number2(ary))
    ary = [1,1,3,3,4,5,5,6,6,8,8]
    print("found: %d" % find_single_number(ary))
    print("found: %d" % find_single_number2(ary))

