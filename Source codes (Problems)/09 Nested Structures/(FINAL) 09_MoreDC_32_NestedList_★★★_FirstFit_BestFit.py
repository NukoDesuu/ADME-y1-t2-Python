def first_fit(L, e):
    if len(L) == 0:
        L.append([e])
    else:
        cur_index = 0
        list_counts = len(L)
        stop = 0
        while cur_index < list_counts and stop != 1:
            list_sum = 0
            cur_list = L[cur_index]
            for n in cur_list:
                list_sum += n
            if list_sum + e <= 100:
                cur_list.append(e)
                stop = 1
            cur_index += 1
        if stop == 0:
            L.append([e])

def best_fit(L, e):
    if len(L) == 0:
        L.append([e])
    else:
        ok_lists = {}
        index = 0
        items = len(L)
        for sublist in L:
            sublist_sum = 0
            for n in sublist:
                sublist_sum += n
            if sublist_sum < 100:
                ok_lists[index] = sublist
            index += 1
        
        ok_lists_sorted = {}
        for i, ok_sublist in ok_lists.items():
            total = sum(ok_sublist) + e
            if total <= 100:
                ok_lists_sorted[i] = total
        if len(ok_lists_sorted) > 0:
            ie = 0
            for j, tot in ok_lists_sorted.items():
                if ie == 0:
                    max_index = j
                    max_value = tot
                    ie = 1
                else:
                    if tot > max_value:
                        max_index = j
                        max_value = tot

            final = []
            index = 0
            while index < items:
                cur_item = L[index]
                if index == max_index:
                    cur_item.append(e)
                final.append(cur_item)
                index += 1
        else:
            L.append([e])

def partition_FF(D):
    ini = D[0]
    temp = [[ini]]

    def all_element_sum(L):
        counts = 0
        for sl in L:
            if len(sl) > 1:
                for e in sl:
                    counts += 1
            counts += 1
        return counts

    items = all_element_sum(temp)
    D.remove(ini)
    for other in D:
        first_fit(temp, other)
        if all_element_sum(temp) == items:
            temp.append([other])
        items = all_element_sum(temp)
    return temp

def partition_BF(D):
    ini = D[0]
    temp = [[ini]]

    def all_element_sum(L):
        counts = 0
        for sl in L:
            if len(sl) > 1:
                for e in sl:
                    counts += 1
            else:
                counts += 1
        return counts

    items = all_element_sum(temp)
    D.remove(ini)
    for other in D:
        best_fit(temp, other)
        if all_element_sum(temp) == items:
            temp.append([other])
        items += 1
    return temp

print(partition_BF([51,60,49,42,49,43,11,31,50,17,13,57,41,27,26,23,23,45,38,50,16,10,18,56,44,49,6,23,15,57]))