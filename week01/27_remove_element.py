"""
LeetCode 27. 移除元素（简单）
https://leetcode.cn/problems/remove-element/

题目：原地移除数组 nums 中所有等于 val 的元素，返回新数组的长度。
要求：不能开新数组，必须原地修改，多出来的元素位置不重要。

思路：快慢指针。
    slow 指向"下一个要放有效元素的位置"，初始为 0。
    fast 从头到尾扫一遍：
      - nums[fast] 不等于 val → 这个元素要保留，搬到 nums[slow]，然后 slow 加一
      - nums[fast] 等于 val  → 跳过，slow 不动
    扫完之后，nums 的前 slow 个位置就是保留下来的元素，返回 slow。

复杂度：时间 O(n)（只扫一遍），空间 O(1)（只用了 slow、fast 两个变量）
"""


def removeElement(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow


if __name__ == "__main__":
    cases = [
        ([3, 2, 2, 3], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]),
    ]
    for nums, val, kept in cases:
        result = removeElement(nums, val)
        ok = result == len(kept) and sorted(nums[:result]) == sorted(kept)
        print(f"[{'通过' if ok else '不通过'}] 输入 {nums}，val={val} → 返回 {result}，期望 {len(kept)}")