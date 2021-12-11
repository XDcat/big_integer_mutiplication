from cmath import cos, sin, pi, exp
from typing import List
from numpy.fft import fft, ifft

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 设置字符串长度为 2 的整数幂（这样才能分治）
        N1, N2 = len(num1), len(num2)
        Nt = max(N1, N2)
        N = 1
        while N < Nt:
            N = N << 1
        N = N << 1

        num1 = "0" * (N - N1) + num1
        num2 = "0" * (N - N2) + num2

        # 构造系数表达式
        xishu1 = [int(i) for i in num1[::-1]]
        xishu2 = [int(i) for i in num2[::-1]]


        # 使用 FFT 得到点值表达式
        dianzhi1 = self.FFT(xishu1, False)
        dianzhi2 = self.FFT(xishu2, False)

        print("自己的FFT")
        print(dianzhi1)
        print(dianzhi2)
        print("numpy 的FFT")
        print(fft(xishu1).tolist())
        print(fft(xishu2).tolist())

        # 求出结果的点值表达式
        dianzhi3 = []
        for i in range(N):
            dianzhi3.append(dianzhi1[i] * dianzhi2[i])

        # 使用逆 FFT，求出结果系数表达式
        xishu3 = self.FFT(dianzhi3, True)
        print("自己的 IFFT")
        print(xishu3)
        print("numpy 的 IFFT")
        print(ifft(dianzhi3).tolist())

        # res = "".join(xishu3[::-1])
        res = xishu3
        res = [round(i.real * len(dianzhi1)) for i in res[::-1]]

        i = 0
        for i in range(len(res)):
            if res[i] != 0:
                break
        res = "".join([str(j) for j in res[i:]])
        return res

    def FFT(self, a: List, flag: bool) -> List:
        """快速傅里叶变换(求值)，从系数映射到y，得到点值表示法
        :param a: 系数项 或者 y
        :param flag: 是否求逆
        """
        n = len(a)
        if n == 1:
            return a

        # omg_n = complex(cos(2 * pi / n), sin(2 * pi / n))
        omg_n = exp(2 * pi * 1j / n)
        if flag:
            # 逆 FFT
            omg_n = 1 / omg_n
        # 旋转因子，后续会使用 omg_n 进行更新
        omg = 1

        # 系数项划分为偶数和奇数项
        a0 = a[::2]  # 偶数项
        a1 = a[1::2]  # 奇数项

        # 奇偶系数项对应的 y
        y0 = self.FFT(a0, flag)
        y1 = self.FFT(a1, flag)

        res = [0] * n
        for k in range(n // 2):
            res[k] = y0[k] + omg * y1[k]
            res[k + n // 2] = y0[k] - omg * y1[k]
            omg = omg * omg_n

        # 逆 FFT
        if flag:
            res = [i / n for i in res]
        return res


if __name__ == '__main__':
    import random

    # for i in range(5):
    #     num1 = "".join([str(random.randint(0, 10)) for _ in range(random.randint(50, 101))])
    #     num2 = "".join([str(random.randint(0, 10)) for _ in range(random.randint(50, 101))])
    #     res = Solution().multiply(num1, num2)
    #     print(f"num1 = {num1}")
    #     print(f"num2 = {num2}")
    #     print(f"num1 * num2 = {res}")
    #     print("系统校验:", int(num1) * int(num2))
    #     print()

    num1 = "123"
    num2 = "456"
    res = Solution().multiply(num1, num2)
    print(f"num1 = {num1}")
    print(f"num2 = {num2}")
    print(f"num1 * num2 = {res}")
    print("系统校验:", int(num1) * int(num2))
    print()

