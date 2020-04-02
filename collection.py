def cal(a, op, b):
    return {
        '+': a + b,
        '-': a - b,
        '*': a * b
    }[op]

def solve():
    pass

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)
def lcm3(a,b,c):
    return lcm(a,lcm(b,c))

if  __name__ == '__main__' :
    solve()

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()


    def percDown(hole,heap=[]):#heap[0]没有元素
        child=0
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

    def buildHeap(arr=[]):#arr[0]没有元素，实际元素个数是len-1
        i=int((len(arr)-1)/2)
        while i>=1:
            percDown(i,arr)
            i-=1
def unjoset():
    n=0
    root=[-1 for i in range(n)]

    def rootOf(a):
        if root[a]==-1:
            return a
        return rootOf(root[a])

    def combin(a,b):
        root1=rootOf(a)
        root2=rootOf(b)
        if root1==root2:
            return False
        root[root2]=root1
        return True

import sys

src = sys.stdin.readlines()
src = list(map(lambda x: x.strip('\n'), src))
print(src)



#########################################################################
n, m = map(int, input().split())
weight = list(map(lambda x: int(x), input().split()))
edges = [[0 for i in range(n)] for j in range(n)]

# 初始化边
cur = []
for i in range(n - 1):
    edge = list(map(int, input().split()))
    edges[edge[0] - 1][edge[1] - 1] = 1
    edges[edge[1] - 1][edge[0] - 1] = 1


# 寻找路线方法
def find(fr, to, p):
    nonlocal cur
    if fr == to:
        cur = p
        return
    for ne in range(n):
        if edges[fr][ne] == 1 and not (ne in p):
            find(ne, to, p + [ne])