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
    
test =[1, "a", 3, 4, 5]
bubble_sort(test)
selection_sort(test)
print test