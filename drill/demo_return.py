"""
小实验：return 到底什么时候要写？
运行：python drill/demo_return.py
"""


def 有返回值():
    return 5


def 没返回值():
    x = 1 + 1          # 算了点东西，但没有把结果交出去


a = 有返回值()
b = 没返回值()

print(f"有返回值() 交出来的东西是：{a}")
print(f"没返回值() 交出来的东西是：{b}")

print()
print("=" * 46)
print("对照你做过、要做做的三道题")
print("=" * 46)
print("27  题目要「新长度」     -> 需要 return slow")
print("26  题目要「新长度」     -> 需要 return slow")
print("283 题目什么都不要，")
print("    只要求把数组改好     -> 不需要 return")
print()
print("怎么判断？回头看题目里有没有问「返回什么」。")
print("题目在问你要一个数字，就要 return；")
print("题目只说「把数组改成什么样」，就不用 return。")