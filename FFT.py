from cmath import cos, sin, pi, exp
from typing import List

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 设置字符串长度为 2 的整数幂（这样才能分治）
        N1, N2 = len(num1), len(num2)
        Nt = max(N1, N2)
        N = 1
        while N < Nt:
            N = N << 1
        N = N << 1

        # 为数字补长度
        num1 = "0" * (N - N1) + num1
        num2 = "0" * (N - N2) + num2

        # 构造系数表达式
        xishu1 = [int(i) for i in num1[::-1]]
        xishu2 = [int(i) for i in num2[::-1]]


        # 使用 FFT 得到点值表达式
        dianzhi1 = self.FFT(xishu1, False)
        dianzhi2 = self.FFT(xishu2, False)


        # 求出结果的点值表达式
        dianzhi3 = []
        for i in range(N):
            dianzhi3.append(dianzhi1[i] * dianzhi2[i])

        # 使用逆 FFT，求出结果系数表达式
        xishu3 = self.FFT(dianzhi3, True)

        # 带入 x = 10, 求出结果
        res = 0
        for i in xishu3[::-1]:
            res = 10 * (round(i.real) + res)
        res = res / 10
        res = int(res)

        return str(res)

    def FFT(self, a: List, flag: bool) -> List:
        """快速傅里叶变换(求值)，从系数映射到y，得到点值表示法
        :param a: 系数项 或者 y
        :param flag: 是否求逆
        """
        y = self.FFTRecursion(a, flag)

        # IFFT
        n = len(a)
        if flag:
            y = [i / n for i in y]
        return y

    def FFTRecursion(self, a: List, flag: bool) -> List:
        """递归实现FFT"""
        n = len(a)
        if n == 1:
            return a

        # 复数根
        # omg_n = exp(-2 * pi * 1j / n)
        omg_n = cos(2*pi / n) + 1j * sin(2*pi / n)
        if flag:
            # IFFT
            omg_n = 1 / omg_n
        omg = 1

        # 分为奇偶两个部分
        a0 = a[::2]  # even
        a1 = a[1::2]  # odd

        # 计算两个部分的y值
        y0 = self.FFTRecursion(a0, flag)
        y1 = self.FFTRecursion(a1, flag)

        # 计算最终结果的y
        y = [0] * n
        for k in range(n // 2):
            y[k] = y0[k] + omg * y1[k]
            y[k + n // 2] = y0[k] - omg * y1[k]
            omg = omg * omg_n
        return y

if __name__ == '__main__':
    import random

    for i in range(5):
        num1 = "".join([str(random.randint(0, 10)) for _ in range(random.randint(50, 101))])
        num2 = "".join([str(random.randint(0, 10)) for _ in range(random.randint(50, 101))])
        res = Solution().multiply(num1, num2)
        print(f"num1 = {num1}")
        print(f"num2 = {num2}")
        print(f"num1 * num2 = {res}")
        system_mutiplication = int(num1) * int(num2)
        print("系统校验:", system_mutiplication)
        print("差值:", abs(system_mutiplication - int(res)))
        print("误差率:", abs(system_mutiplication - int(res))/ system_mutiplication)
        print()

    # num1 = "1232343045839205428"
    # num2 = "4567890987890"
    # res = Solution().multiply(num1, num2)
    # print(f"num1 = {num1}")
    # print(f"num2 = {num2}")
    # print(f"num1 * num2 = {res}")
    # print("系统校验:", int(num1) * int(num2))
    # print()
    #
