def swap (list, idx_i, idx_j):
    list_len = len(list)
    if idx_i > list_len or idx_j > list_len or idx_i < 0 or idx_j <0:
        print "invalid index number"
        return
    elif list_len <= 1:
        return
    else:
        temp = list[idx_i]
        list[idx_i] = list[idx_j]
        list[idx_j] = temp

def bubble_sort (list):
    list_len = len(list)
    if list_len <= 1:
        return
    for dummy_element in list:
        swaped = False    
        for idx_i in range(list_len-1):
            if list[idx_i] > list[idx_i+1]:
                swap(list, idx_i, idx_i+1)
                swaped = True
        if swaped == False:
            return           

def selection_sort (list):
    list_len = len(list)
    if list_len <= 1:
        return
    for dummy_element in list:
        max = 0
        for idx_i in range(list_len):
            value = 0
            if list[idx_i] == "a":
                value = 1
            else:
                value = list[idx_i]    
                if value > list[max]:
                    max = idx_i
        swap (list, max, list_len-1)
        list_len -= 1

def insert_sort(list):
    list_len = len(list)
    for idx_i in range(1, list_len):
        idx_j = idx_i
        while list[idx_j] < list[idx_j-1] and idx_j > 0:
            swap (list, idx_j, idx_j-1)
            idx_j -= 1


def binary_search(list, value):
    """
    Find value (first match) in a sorted list
    """
    list_len = len(list)
    idx = -1 
    begin = 0
    end = list_len-1  
    while begin <= end: 
        median = begin + int((end - begin)/2) 
        if value < list[median]:
            end = median - 1 
        elif value > list[median]:
            begin = median + 1
        else:
            idx = median
            return idx

def binary_search_recur_helper(list, begin, end, value):
    median = begin + int((end-begin)/2)
    if begin > end:
        return
    elif value == list[median]:
        return median
    else:
        if value < list[median]:
            return binary_search_recur_helper(list, begin, median-1, value)
        else:
            return binary_search_recur_helper(list, median+1, end, value)

def binary_search_recur (list, value):
    return binary_search_recur_helper(list, 0, len(list)-1, value)

def partition_slow (list, begin, end):
    """
    take a list, put the first element of the list to a position that all elements on its left is smaller
    than it and all the elements on its right is bigger, the order of all other elements does not
    matter. the funciton returns the first element's index after partition process
    """
    list_len = len(list)
    first_element = list[begin]
    for index_i in range (begin+1, end+1):
        index_j = index_i
        while list[index_j] > list[index_j-1] and index_j > begin:
            if list[index_j]== first_element:
                break
            else:
                index_j -=1
        while list[index_j] < list[index_j-1] and index_j > begin:
            swap (list, index_j, index_j-1)
            if list[index_j]== first_element:
                break
            else:
                index_j -=1
    return index_j

def partition (list, begin, end):
    key = list[begin]
    idx_i = begin + 1
    idx_j = begin + 1
    while idx_i < len(list):
        if list[idx_i] < key:
            swap(list, idx_i, idx_j)
            idx_i +=1
            idx_j +=1
        elif list[idx_i] > key:
            idx_i +=1  
    swap (list, begin, idx_j-1)
    return idx_j-1

def quick_sort(list, begin, end):
    if begin >= end:
        return
    else:
        pivot = partition(list, begin, end)
        quick_sort (list, begin, pivot-1)
        quick_sort (list, pivot+1, end)

def merge_list(list, begin1, end1, begin2, end2):
    """
    This function takes a list, and two interval (begin1-end1, begin2-end2).
    the elements within the interval are sorted. 
    The two interval are neighers(end1+1 = begin2). 
    Sort for all elements of both interval and put them back to the list in 
    sorted order, and return the list.
    """
    temp_list = []
    idx_i = begin1
    idx_j = begin2
    while idx_i <= end1 and idx_j <= end2:
        if list[idx_i] <= list[idx_j]:
            temp_list.append(list[idx_i])
            idx_i += 1
        else:
            temp_list.append(list[idx_j])
            idx_j += 1
    if idx_i > end1:
        while idx_j <= end2:
            temp_list.append(list[idx_j])
            idx_j += 1
    elif idx_j > end2:
        while idx_i <= end1:
            temp_list.append(list[idx_i])
            idx_i += 1
    idx_temp = 0
    for idx in range (begin1, end2+1):
        list[idx] = temp_list[idx_temp]
        idx_temp += 1

def merge_sort (list, begin, end):
    if begin >= end:
        return
    else:
        median = begin+(end-begin)/2
        merge_sort(list, begin, median)
        merge_sort(list, median+1, end)
        merge_list(list, begin, median, median+1, end)


test1 =[5,4,3,2,1]
test2 = [1,2,3,4,5]
test3 = [3,5,7,1,2,0,9]
test4 = [2,3,4,5]
test5 = [5,9,4,5,6,7,1,2,0]
test6 = [1,3,5,7,9,2,4,6,8,10]
test7 = [1]
test8 = [3,1]

merge_sort(test3, 0, 6)
print test3

