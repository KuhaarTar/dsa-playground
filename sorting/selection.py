def selection_sort(nums: list):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


print(selection_sort([7, 45, 2, 1, -5, -9, 7, 0, 23]))
