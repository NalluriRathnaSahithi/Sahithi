def duplicate(l):
    l1=[]
    for i in l:
        if(i not in l):
            l1.append(i)
    print(l1)