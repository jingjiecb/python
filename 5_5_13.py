# https://www.coordinate.wang/index.php/archives/2662/
# 动态规划方法。遍历数组，每次看一下等差数列上一个结果是不是在，如果在就接上，如果不在就从这个位置开始新建一个等差数列。
def solve():
    nums=list(map(int,input().split(',')))
    dif=int(input())
    mem,res={},1
    for i in nums:
        if i-dif in mem:
            mem[i]=mem[i-dif]+1
        else:
            mem[i]=1
        res=max(res,mem[i])
    print(res)

if  __name__ == '__main__' :
    solve()