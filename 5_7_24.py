def solve():
    n,m=map(int,input().split())
    weight=list(map(lambda x:int(x),input().split()))
    edges=[[0 for i in range(n)] for j in range(n)]

    # 初始化边
    cur=[]
    for i in range(n-1):
        edge=list(map(int,input().split()))
        edges[edge[0]-1][edge[1]-1]=1
        edges[edge[1]-1][edge[0]-1]=1

    # 寻找路线方法
    def find(fr,to,p):
        nonlocal cur
        if fr==to:
            cur= p
            return
        for ne in range(n):
            if edges[fr][ne]==1 and not (ne in p):
                find(ne,to,p+[ne])

    def getV(p,k):
        ws=list(map(lambda x:weight[x],p))
        ws.sort()
        return ws[k-1]

    last=0
    for i in range(m):
        u,v,k=map(int,input().split())
        ru=u ^ last
        find(ru-1,v-1,[ru-1])
        here=getV(cur,k)
        last=here
        print(here)

if __name__ == '__main__':
    solve()