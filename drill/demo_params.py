"""
小演示：函数参数到底是什么？
运行：python drill/demo_params.py
"""


def show(nums, val):
    print(f"  [进入函数] nums = {nums}，val = {val}")
    print(f"  [进入函数] nums 的类型是 {type(nums)}")
    nums.append(999)
    print(f"  [函数内部] 我改了 nums，现在是 {nums}")


print("=" * 46)
print("演示 1：把 a 传进去")
print("=" * 46)
a = [3, 2, 2, 3]
print(f"[外面] 调用之前：a = {a}")
show(a, 3)
print(f"[外面] 调用之后：a = {a}   <-- 外面的 a 也被改了！")

print()
print("=" * 46)
print("演示 2：把 b 传进去")
print("=" * 46)
b = [1, 1, 2]
print(f"[外面] 调用之前：b = {b}")
show(b, 1)
print(f"[外面] 调用之后：b = {b}")

print()
print("=" * 46)
print("演示 3：不经过变量，直接把列表写进括号")
print("=" * 46)
show([9, 9, 9], 9)