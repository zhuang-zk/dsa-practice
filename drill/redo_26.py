"""
默写练习：LeetCode 26. 删除有序数组中的重复项（简单）
https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

要求：不看 week01/26_remove_duplicates.py，从零写出来。

题目：原地删除有序数组中的重复元素，每个元素只留一次，返回新长度。

只在你完全没思路时才看这一行提示：
    slow 是有效区长度；比较对象是 nums[slow - 1]，不是 nums[slow]。
"""


def removeDuplicates(nums):
    # 在这里写你的代码
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
        ([1], [1]),
        ([1, 1], [1]),
    ]
    for nums, kept in cases:
        original = nums[:]
        result = removeDuplicates(nums)
        ok = result == len(kept) and nums[:result] == kept
        print(f"[{'通过' if ok else '不通过'}] 输入 {original} → 返回 {result}，期望 {len(kept)}")
