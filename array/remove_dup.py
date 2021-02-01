#!/usr/bin/python3

def remove_duplicates(ary):
    num = ary[0]
    real_tail = 1
    for i in range(1, len(ary)):
        if num != ary[i]:
            num = ary[real_tail] = ary[i]
            real_tail += 1
    return ary[:real_tail]

def remove_more_than_two_duplicates(ary):
    num = ary[0]
    real_tail = 1
    dup_count = 1
    for i in range(1, len(ary)):
        if num != ary[i]:
            num = ary[real_tail] = ary[i]
            real_tail += 1
            dup_count = 1
        else:
            dup_count += 1
            if dup_count <= 2:
                ary[real_tail] = ary[i]
                real_tail += 1
    return ary[:real_tail]

if __name__ == '__main__':
    ary = [1,1,2,3,3,4,6,6,8,8]
    print("ary: ", remove_duplicates(ary))

    ary = [1,1,1,1,2,2,3,4,4,4,6,8,8]
    print("ary: ", remove_more_than_two_duplicates(ary))

