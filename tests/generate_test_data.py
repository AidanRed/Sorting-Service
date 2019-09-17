if __name__ == "__main__":
    import random

    def is_sorted(the_list):
        return all(the_list[i] <= the_list[i+1] for i in range(len(the_list)-1));

    to_write = ""
    for i in range(10):
        data = []
        # Ensure data isn't accidentally sorted
        while is_sorted(data):
            data = [random.randint(1, 1000) for x in range(20)]
        
        to_write += str(data)[1:-1] + "\n"
    
    with open("algorithm_test_data.txt" , "w") as data_file:
        data_file.write(to_write)
