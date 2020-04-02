def solve():
    n=int(input())
    res=float('inf')
    if n==1:
        print(0,end='')
        return
    res=float('inf')
    board1 = int(n ** 0.5)
    board=int(n/2)

    for i in range(1,board):
        cur=gcd(n,i)
        if cur!=0:
            if res>cur:
                res=cur
            else:
                break

    print(res-1,end='')

def gcd(a,b):
    res=0
    while b:
        res+=int(a/b)
        a,b=b,a%b
    if a==1:
        return res
    else:
        return 0

if __name__ == '__main__':
    solve()