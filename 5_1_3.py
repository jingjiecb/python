def solve():
    lists=[]
    pointer=[]
    total=0
    res=[]
    strl=list(map(lambda x:x[0:-2],input().split('[')[2:]))

    for strs in strl:
        temp=list(map(int,strs.split(',')))[::-1]
        lists.append(temp)
        pointer.append(len(temp)-1)
        total+=len(temp)

    while total>0:
        index=-1
        min=255
        for i in range(len(lists)):
            current=lists[i][pointer[i]]
            if current<min:
                min=current
                index=i
        res.append(min)
        pointer[index]-=1
        if pointer[index]<0:
            del lists[index]
            del pointer[index]
        total-=1

    print(res)




if __name__=='__main__':
    solve()
