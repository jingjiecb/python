# https://www.luogu.com.cn/blog/KonjacWyx/solution-p2767
def solve():
    n,m=map(int,input().split())
    c1=m*n
    res=1
    for i in range(1,n):
        res*=c1
        res=int(res/i)
        c1-=1
    res=int(res/n)
    print(res%10007)

if  __name__ == '__main__' :
    solve()