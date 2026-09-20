"""
第 1 周交付：猜数字游戏
运行：python week01/guess_number.py

玩法
    程序随机想一个 1-100 的整数，你来猜。
    每次猜完，程序告诉你「大了」还是「小了」。
    猜中后，程序告诉你一共用了几次。

用到的知识点
    random.randint(1, 100)      生成 1~100 的随机整数，两边都能取到
    input("提示语")              等你在终端打字，返回的是【字符串】
    int(...)                    把字符串转成整数
    while True + break          一直循环，猜中才跳出去
    f-string                    print(f"...{count}...") 花括号里放变量

易错点
    1. input() 拿到的是字符串，必须套 int() 才能比大小
    2. count += 1 要放在读入之后、判断之前，次数才不会数错
    3. break 必须写在 else 分支里，否则循环停不下来
"""

import random


def guess_number():
    answer = random.randint(1, 100)
    count = 0

    while True:
        guess = int(input("请输入："))
        count += 1

        if guess > answer:
            print("大了！")
        elif guess < answer:
            print("小了！")
        else:
            print(f"猜对了！你一共猜了 {count} 次")
            break


if __name__ == "__main__":
    guess_number()