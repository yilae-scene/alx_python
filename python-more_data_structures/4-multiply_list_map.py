# a function that uses map() to iterate
def multiply_list_map(my_list=[], num=0):
    return list(map(lambda x: x * num, my_list))
