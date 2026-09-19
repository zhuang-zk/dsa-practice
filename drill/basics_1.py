"""
实验文件：随便改，改坏了也没关系，重新运行就行。
运行命令：python drill/basics_1.py
"""

print("=" * 46)
print("第 1 步：参数 = 填空")
print("=" * 46)


def 打招呼(谁):
    print("你好，" + 谁)


打招呼("小明")
打招呼("小红")
打招呼("老师")
# 试着把上面三个名字改成你自己的，再运行一次


print()
print("=" * 46)
print("第 2 步：把填空换成列表")
print("=" * 46)


def 数一数(nums):
    print(f"我收到的 nums 是 {nums}，它有 {len(nums)} 个元素")


数一数([3, 2, 2, 3])
数一数([1, 2, 3, 4, 5])
# 试着把上面两个列表换成你自己编的，再运行一次


print()
print("=" * 46)
print("第 3 步：回到题目里的 removeElement")
print("=" * 46)


def removeElement(nums, val):
    print(f"  [函数内部] 收到 nums = {nums}，val = {val}")
    return 0


print(">> 本地测试时，是我们自己调用它：")
removeElement([3, 2, 2, 3], 3)

print()
print(">> 在力扣网站上，是力扣调用它：")
print("   你点「提交」以后，力扣就拿着它自己准备的测试数据，")
print("   一遍一遍地调用你的 removeElement(nums, val)。")
print("   所以函数里的 nums，永远是力扣这一次喂进来的那个数组。")