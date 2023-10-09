def find_max_count(d):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    a=0
    ma=d[0]
    while a<len(d):
        if ma<=d[a]:
            ma=d[a]
        a+=1
    
    
    return d.count(ma)
print (find_max_count([2,4,6,76543,76543,76543]))
