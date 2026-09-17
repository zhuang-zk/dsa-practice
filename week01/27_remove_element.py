"""
LeetCode 27. 移除元素（简单）
https://leetcode.cn/problems/remove-element/

题目：原地移除数组 nums 中所有等于 val 的元素，返回新数组的长度。
要求：不能开新数组，必须原地修改，多出来的元素位置不重要。

思路：（先用中文把你的想法写在这里，再动手写代码）


复杂度：时间 O(n)，空间 O(1)

提示：快慢指针。slow 指向"下一个要放有效元素的位置"，
      fast 一路往后扫，遇到不等于 val 的元素就放到 slow 处。
"""


def removeElement(nums, val):
    # TODO: 在这里写你的代码
    pass


if __name__ == "__main__":
    cases = [
        ([3, 2, 2, 3], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]),
    ]
    for nums, val, kept in cases:
        result = removeElement(nums, val)
        ok = result == len(kept) and sorted(nums[:result]) == sorted(kept)
        print(f"[{'通过' if ok else '不通过'}] 输入 {nums}，val={val} → 返回 {result}，期望 {len(kept)}")