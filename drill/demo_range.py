"""
小实验：range(nums) 到底行不行？
运行：python drill/demo_range.py
"""

nums = [3, 2, 2, 3]
print(f"nums = {nums}")

print()
print("-" * 46)
print("写法 A：for fast in range(nums)")
print("-" * 46)
try:
    for fast in range(nums):
        print(fast)
except TypeError as e:
    print(f"  报错：{e}")
print("  原因：range() 只接受整数，而 nums 是一个列表")

print()
print("-" * 46)
print("写法 B：for fast in range(len(nums))   <- 正确写法")
print("-" * 46)
print(f"  len(nums) 的结果是 {len(nums)}，这是个整数")
print(f"  range({len(nums)}) 生成 {list(range(len(nums)))}，也就是所有下标")
for fast in range(len(nums)):
    print(f"    fast = {fast}，nums[{fast}] = {nums[fast]}")

print()
print("-" * 46)
print("写法 C：for fast in nums")
print("-" * 46)
for fast in nums:
    print(f"    fast = {fast}   <- 拿到的是「值」，不是「下标」")

print()
print("-" * 46)
print("用写法 C 试着解 27 题，居然也过了：")
print("-" * 46)


def removeElement(nums, val):
    slow = 0
    for x in nums:
        if x != val:
            nums[slow] = x
            slow += 1
    return slow


data = [3, 2, 2, 3]
result = removeElement(data, 3)
print(f"  输入 [3, 2, 2, 3]，val=3 -> 返回 {result}，数组变成 {data}")