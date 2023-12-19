def bubble_sort(nums: list):
    n = len(nums)
    for pass_num in range(n - 1, 0, - 1):
        for i in range(pass_num):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


print(bubble_sort([7, 45, 2, 1, -5, -9, 7, 0, 23]))
