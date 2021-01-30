#!/usr/bin/python


def find_single_number(ary):
    if ary[0] != ary[1]:
        print ary[0]

    prev = ary[0]
    flag = False

    for i in ary[1:]:

        #if flag == True and prev != i:
        #    print i
        #    flag = False
        #elif prev != i:
        #    flag = True
        #prev = i

        if flag == True:
            if prev != i:
                print prev
            flag = False
        else:
            if prev != i:
                flag = True

        prev = i

    if flag == True:
        print ary[len(ary)-1]

if __name__ == '__main__':
    a = [3,7,7,9,9,8,6,6,5]
    find_single_number(a)

