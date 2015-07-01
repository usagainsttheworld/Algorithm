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


test =[1, 2, 3, 8, 9]
#bubble_sort(test)
#selection_sort(test)
#insert_sort(test)
#print binary_search(test,11)
print binary_search_recur(test, 22)
