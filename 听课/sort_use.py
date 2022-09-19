def numeric_compare(x, y):
    return x - y
    
sorted([5, 2, 4, 1, 3], cmp=numeric_compare) 