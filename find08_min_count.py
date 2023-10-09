def find_min_count(d):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    a=0
    mi=d[0]
    while a<len(d):
        if mi<=d[a]:
            mi=d[a]
        a+=1
    return d.count(mi) 
print (find_min_count([3,4,2,5,6,7,3]))