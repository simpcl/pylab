package main

import (
	"fmt"
	"testing"
)

func FindSingleNumber(ary []int) int {
	begin := 0
	end := len(ary)
	var mid int = 0

	for {
		if (end - begin) == 1 {
			return ary[begin]
		} else if (end - begin) <= 0 {
			return -1
		}

		mid = int((begin + end) / 2)

		//fmt.Printf("begin: %d, end: %d, mid: %d\n", begin, end, mid)

		if (mid-begin)%2 == 0 {
			if ary[mid] == ary[mid-1] {
				end = mid - 1
			} else if ary[mid] != ary[mid+1] {
				return ary[mid]
			} else {
				begin = mid + 2
			}
		} else {
			if ary[mid] == ary[mid-1] {
				begin = mid + 1
			} else if ary[mid] != ary[mid+1] {
				return ary[mid]
			} else {
				end = mid
			}
		}
	}

	return -1
}

func TestFindSingleNumber(t *testing.T) {
	ary := []int{1, 1, 2, 2, 3, 3, 4, 4, 8}
	num := FindSingleNumber(ary)
	fmt.Printf("found: %d\n", num)
}
