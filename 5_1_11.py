def solve():
    input()
    nums = list(map(int, input().split()))

    total=0
    steps=[]

    for i in range(len(nums),-1,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                total+=1
                steps.append()


if  __name__ == '__main__' :
    solve()