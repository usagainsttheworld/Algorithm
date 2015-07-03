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

test =[5,4,3,2,1]
test_b = [1,2,3,4,5]
test_r = [3,5,7,1,2,0,9]
test_p = [2,3,4,5]
#bubble_sort(test)
#selection_sort(test)
#insert_sort(test)
#print binary_search(test,11)
#print binary_search_recur(test, 22)
#print partition(test_r, 0, 4)
quick_sort(test_r, 0, len(test_r)-1)
print test_r
