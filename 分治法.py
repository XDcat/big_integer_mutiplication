class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 终止条件
        if min(len(num1), len(num2)) == 1:
            res = int(num1) * int(num2)
            # print(f"{num1}*{num2} = {res}")
            return str(res)

        # 将 num1 和 num2 的长度相同，并设置为2的倍数
        N1 = len(num1)
        N2 = len(num2)
        N = max(N1, N2)
        if N1 > N2:
            num2 = "0" * (N1 - N2) + num2
        elif N1 < N2:
            num1 = "0" * (N2 - N1) + num1

        if N % 2 == 1:
            num1 = "0" + num1
            num2 = "0" + num2
            N = len(num1)

        n = N >> 1  # 2 整除, 二分字符串
        # 切分
        a1, a2 = num1[:n], num1[n:]
        b1, b2 = num2[:n], num2[n:]
        # 计算小项
        a1b1 = self.multiply(a1, b1)
        a1b1 = int(a1b1)
        a2b2 = self.multiply(a2, b2)
        a2b2 = int(a2b2)

        middle = (int(a1) - int(a2)) * (int(b2) - int(b1)) + a1b1 + a2b2

        # 结果
        res = a1b1 * pow(10, N) + middle * pow(10, n) + a2b2
        # print(f"{num1}*{num2} = {res}")
        return str(res)


if __name__ == '__main__':
    import random

    for i in range(5):
        num1 = "".join([str(random.randint(0, 10)) for _ in range(random.randint(50, 101))])
        num2 = "".join([str(random.randint(0, 10)) for _ in range(random.randint(50, 101))])
        res = Solution().multiply(num1, num2)
        print(f"num1 = {num1}")
        print(f"num2 = {num2}")
        print(f"num1 * num2 = {res}")
        print("系统校验:", int(num1) * int(num2))
        print()
