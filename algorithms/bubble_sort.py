def sort(the_list):
    def swap(x, y):
        the_list[x], the_list[y] = the_list[y], the_list[x]

    list_length = len(the_list)
    unsorted_end = list_length

    made_change = True
    while made_change:
        made_change = False

        for i in range(1, unsorted_end):
            if (the_list[i-1] > the_list[i]):
                swap(i-1, i)
                made_change = True
        
        unsorted_end -= 1
    
    return the_list