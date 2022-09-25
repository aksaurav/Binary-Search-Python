# Implementation of binary search algorithm!

# We will prove that binary search is faster than naive search!

# naive search: scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then retun - 1
import random
import time


def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)): # every single index
        if l[i] == target: # if 'l' at that index == target
            return i
    return -1


# binary search uses dived and conquer!
# we will leverage the fact that our list is SORTED

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0 # if our target is low we want to check the lowest possible index at that list
    if high is None:
        high = len(l) -1 # if our target is == high we want to chekc the highest possible index we can [-1 is referering to the highest index in the list]

    if high < low:
        return -1
    # example l = [1, 3, 5, 10, 12]  should return 3
    midpoint = (low + high) // 2 # 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)

if __name__ == '__main__':
    # l = [1, 3, 5, 10, 12]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))
    lenght = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < lenght:
        sorted_list.add(random.randint(-3*lenght, 3*lenght))
    sorted_list = sorted(list(sorted_list))


    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/lenght, "seconds")


    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/lenght, "seconds")