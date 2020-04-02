def solve():
    tree1=[0]+eval(input())
    tree2=[0]+eval(input())

    buildHeap(tree1)
    buildHeap(tree2)
    res=[]

    while len(tree1)>1 and len(tree2)>1:
        a=tree1[1]
        b=tree2[1]
        if a>b:
            res.append(b)
            hpop(tree2)
        else:
            res.append(a)
            hpop(tree1)

    if len(tree1)==1:
        while len(tree2)>1:
            res.append(hpop(tree2))

    if len(tree2)==1:
        while len(tree1)>1:
            res.append(hpop(tree1))

    print(res)


def percDown(hole,heap):#heap[0]没有元素
    tmp=heap[hole]
    currentSize=len(heap)-1
    while hole*2<=currentSize:
        child=hole*2
        if child!=currentSize:
            if heap[child+1]<heap[child]:
                child+=1
        if heap[child]<tmp:
            heap[hole]=heap[child]
            hole=child
        else:
            break
    heap[hole]=tmp

def buildHeap(arr):#arr[0]没有元素，实际元素个数是len-1
    i=int((len(arr)-1)/2)
    while i>=1:
        percDown(i,arr)
        i-=1

def hpop(heap):
    i=len(heap)-1
    res=heap[1]
    heap[1]=heap[i]
    del heap[i]
    if len(heap)>2:
        percDown(1,heap)
    return res

if  __name__ == '__main__' :
    solve()