def sort(the_list):
    for index in range(1, len(the_list)):
        value = the_list.pop(index)

        prev_index = index - 1
        while prev_index >= 0 and value < the_list[prev_index]:
            prev_index -= 1
        
        the_list.insert(prev_index+1, value)
    
    return the_list