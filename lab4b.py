#!/usr/bin/env python3

def join_lists(l1, l2):
    
    return list(set(l1) | set(l2))  # Using set to eliminate duplicates

def match_lists(l1, l2):
    
    return list(set(l1) & set(l2))  # Intersection of two sets

def diff_lists(l1, l2):
    
    return list(set(l1) ^ set(l2))  # Symmetric difference

if __name__ == '__main__':
    list1 = list(range(1, 10))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = list(range(5, 15))   # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))
