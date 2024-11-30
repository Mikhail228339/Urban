my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

def pos(lst):
    return [x for x in lst if x > 0] or None
pos([42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5])

print(pos(my_list))