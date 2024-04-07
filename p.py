def unique(m):
    tmplist=[]
    for i in m:
        if not(i in tmplist):
            tmplist.append(i)
    return tmplist

l=[1,1,2,3,4,4,5,6,7,7,8]
unique(l)
print(unique(l))

