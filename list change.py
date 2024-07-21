li = [ 12,35,9,56,24]

def myfun(li):
    si = len(li)
    
    tmp = li[0]
    li[0] =li[si-1]
    li[si -1] = tmp
    
    return li
print(myfun(li))