"""
第 2 周基础知识：函数作用域
运行：python drill/scope_basics.py

一句话：函数里的变量名，和外面的变量名，默认是两套东西。
"""

print("=" * 56)
print("第 1 部分：函数能「读」外面的变量")
print("=" * 56)

x = 10


def read_x():
    print(f"    函数里读到 x = {x}")


print(f"    外面 x = {x}")
read_x()

print()
print("=" * 56)
print("第 2 部分：函数里「赋值」= 新建一个局部变量")
print("=" * 56)


def write_x():
    x = 99
    print(f"    函数里 x = {x}")


print(f"    调用前，外面 x = {x}")
write_x()
print(f"    调用后，外面 x = {x}   <- 没变！")

print()
print("=" * 56)
print("第 3 部分：但「修改可变对象」会影响外面")
print("=" * 56)

nums = [1, 2, 3]


def modify_list():
    nums.append(4)
    print(f"    函数里 nums = {nums}")


def rebind_list():
    nums = [9, 9, 9]
    print(f"    函数里 nums = {nums}")


print(f"    初始 nums = {nums}")
modify_list()
print(f"    append 之后，外面 nums = {nums}      <- 变了！")
rebind_list()
print(f"    重新赋值之后，外面 nums = {nums}   <- 没变！")

print()
print("=" * 56)
print("第 4 部分：一个比喻")
print("=" * 56)
print("""
    把变量名想成一根「线」，另一头牵着某个东西。

        x  ──────>  10
        nums ────>  [1, 2, 3]   （列表）

    「赋值」= 把线改牵到别的东西上
        x = 99           函数里的线改牵 99，外面那根线还牵着 10
        nums = [9,9,9]   函数里的线改牵新列表，外面那根线还牵着老列表

    「修改内容」= 顺着线找到那个东西，动手改它
        nums.append(4)   顺着线摸到那个列表，往里面加东西，
                         外面那根线牵着的是同一个列表，所以看得见
""")

print()
print("=" * 56)
print("第 5 部分：回到你做过的题")
print("=" * 56)


def removeElement(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]     # 修改内容 -> 外面看得见
            slow += 1
    return slow                         # 数字改不了，只能 return 交出去


data = [3, 2, 2, 3]
print(f"    调用前 data = {data}")
result = removeElement(data, 3)
print(f"    调用后 data = {data}   <- 外面变了，因为往列表里写了东西")
print(f"    返回值        = {result}         <- 数字没法「修改」，只能 return")