'''
10
same as count and say in leetcode
'''
nums = [1]
for iter in xrange(30):
    p = nums[0]
    count = 0
    i = 0
    nums_new = []
    while i < len(nums):
        if nums[i] == p:
            count += 1
        else:
            nums_new.append(count)
            nums_new.append(p)
            count = 1
            p = nums[i]
        i += 1
    nums_new.append(count)
    nums_new.append(p)
    if iter == 29:
        print len(nums_new)
    nums = nums_new
    nums_new = []
