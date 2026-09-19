"""
默写练习：LeetCode 27. 移除元素（简单）
https://leetcode.cn/problems/remove-element/

要求：不看 week01/27_remove_element.py，从零写出来。
     卡住超过 10 分钟再看旧代码的思路部分，然后关掉重来。

题目：原地移除数组 nums 中所有等于 val 的元素，返回新数组的长度。
     不能开新数组，多出来的元素位置不重要。
"""


def removeElement(nums, val):
    # 在这里写你的代码
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
        ([1], 1, []),
        ([4, 5], 4, [5]),
    ]
    for nums, val, kept in cases:
        original = nums[:]
        result = removeElement(nums, val)
        ok = result == len(kept) and sorted(nums[:result]) == sorted(kept)
        print(f"[{'通过' if ok else '不通过'}] 输入 {original}，val={val} → 返回 {result}，期望 {len(kept)}")
