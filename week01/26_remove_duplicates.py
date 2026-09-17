"""
LeetCode 26. 删除有序数组中的重复项（简单）
https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

题目：给你一个非严格递增排列的数组 nums，原地删除重复元素，
      使每个元素只出现一次，返回删除后数组的新长度。

思路：快慢指针。slow 是「有效区的长度」，也就是下一个可以写的位置的下标。
      第一个元素一定保留，所以 slow 从 1 开始。
      fast 从下标 1 开始扫，拿 nums[fast] 和有效区最后一个元素 nums[slow-1] 比：
        - 相同 → 重复元素，跳过
        - 不同 → 是新元素，写进 nums[slow]，然后 slow 加一
      扫完后有效区就是去重结果，它的长度 slow 就是答案。

复杂度：时间 O(n)，空间 O(1)

易错点：比较的对象必须是 nums[slow-1]（刚写进去的最新值），
        写成 nums[slow] 会拿到还没被覆盖的旧数据，导致误判。
"""


def removeDuplicates(nums):
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow


if __name__ == "__main__":
    cases = [
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
    ]
    for nums, kept in cases:
        result = removeDuplicates(nums)
        ok = result == len(kept) and nums[:result] == kept
        print(f"[{'通过' if ok else '不通过'}] 输入 {nums} → 返回 {result}，期望 {len(kept)}")