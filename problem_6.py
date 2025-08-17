def can_partition(nums):
    total = sum(nums)

    if total % 2 != 0:
        return False

    target = total // 2
    n = len(nums)

    dp = [False] * (target + 1)
    dp[0] = True  

    for num in nums:
        for s in range(target, num - 1, -1):
            if dp[s - num]:
                dp[s] = True

    return dp[target]

nums = list(map(int, input("Enter numbers separated by space: ").split()))
if can_partition(nums):
    print("true")
else:
    print("false")
