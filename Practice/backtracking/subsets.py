def subsets(nums):
    n = len(nums)
    res, sol = [], []

    def backtrack(i):
        # base case return sol copy
        if i == n:
            res.append(sol[:])
            return

        # left path, don't pick
        backtrack(i + 1)

        # right path, pick
        sol.append(nums[i])
        backtrack(i + 1)

        # backtrack
        sol.pop()

    backtrack(0)
    return res


nums = [1, 2, 3]
print(subsets(nums))
