# https://coordinate.wang/index.php/archives/2387/
# 一种全排列的思路
def solve():
    nums=list(map(int,input().split(',')))
    n=len(nums)
    res=0
    def permute(nums,i):
        nonlocal res
        if i==n:
            res+=1
            return
        for k in range(i,n):
            if i!=k and nums[i]==nums[k]:
                continue
            nums[i],nums[k]=nums[k],nums[i]
            if i==0 or int((nums[i]+nums[i-1])**0.5)**2==(nums[i]+nums[i-1]):
                permute(nums[:],i+1)

    nums.sort()
    permute(nums,0)
    print(res)


if  __name__ == '__main__' :
    solve()