# 参考 https://zhuanlan.zhihu.com/p/42992392
def solve():
    m,n=eval(input())
    if m==0:
        return 0
    ans=n
    while ans>m:
        ans&=(ans-1)
    print(ans)

if  __name__ == '__main__' :
    solve()