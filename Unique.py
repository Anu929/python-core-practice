def four_sum(nums, target):
    result=set() 
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            seen={}  
            for k in range(j+1,len(nums)):
                complement=target-nums[i]-nums[j]-nums[k]
                if complement in seen:
                    quad=tuple(sorted([nums[i],nums[j],nums[k],complement]))
                    result.add(quad)
                seen[nums[k]]=k
    return result
nums=list(map(int, input("Enter numbers separated by space: ").split()))
target=int(input("Enter target: "))
output=four_sum(nums, target)
print("Unique Quadruplets:",output)