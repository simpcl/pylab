#!/usr/bin/python3

def median_of_two_arys(ary1, ary2):
    length = len(ary1) + len(ary2)
    median_index = int(length / 2)
    
    i1 = 0
    i2 = 0
    while (i1 + i2) < median_index:
        if i1 >= len(ary1):
            i2 += 1
            continue
        if i2 >= len(ary2):
            i1 += 1
            continue
        if ary1[i1] < ary2[i2]:
            i1 += 1
        else:
            i2 += 1
    print("median index: %d, i1: %d, i2: %d" % (median_index, i1, i2))
    print("%d %d" % (ary1[i1], ary2[i2]))

if __name__ == '__main__':
    ary1 = [1,3,4,6,10,17,18,20,23,34]
    ary2 = [2,3,5,6,9,11,14,15,20,25,28,29,40,45,50]
    median_of_two_arys(ary1, ary2)
