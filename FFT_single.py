from typing import List
from cmath import pi, exp
from numpy.fft import fft, ifft


def FFTRecursion(a: List, flag: bool) -> List:
    """realize DFT using FFT"""
    n = len(a)
    if n == 1:
        return a

    # complex root
    omg_n = exp(-2 * pi * 1j / n)
    if flag:
        # IFFT
        omg_n = 1 / omg_n
    omg = 1

    # split a into 2 part
    a0 = a[::2]  # even
    a1 = a[1::2]  # odd

    # corresponding y
    y0 = FFTRecursion(a0, flag)
    y1 = FFTRecursion(a1, flag)

    # result y
    y = [0] * n
    for k in range(n // 2):
        y[k] = y0[k] + omg * y1[k]
        y[k + n // 2] = y0[k] - omg * y1[k]
        omg = omg * omg_n
    return y

def FFT(a: List, flag: bool) -> List:
    y = FFTRecursion(a, flag)

    # IFFT
    n = len(a)
    if flag:
        y = [i / n for i in y]
    return y

if __name__ == '__main__':
    test_cases = [
        [1, 1],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [1, 4, 2, 9, 0, 0, 3, 8, 9, 1, 4, 0, 0, 0, 0, 0, ],
    ]

    print("test FFT")
    for i, case in enumerate(test_cases):
        print(f"case{i + 1}", case)
        manual_result = FFT(case, False)
        numpy_result = fft(case).tolist()
        print("manual_result:", manual_result)
        print("numpy_result:", numpy_result)
        print("difference:", [i - j for i, j in zip(manual_result, numpy_result)])
        print()



    print("test IFFT")
    for i, case in enumerate(test_cases):
        print(f"case{i + 1}", case)
        manual_result = FFT(case, True)
        numpy_result = ifft(case).tolist()
        print("manual_result:", manual_result)
        print("numpy_result:", numpy_result)
        print("difference:", [i - j for i, j in zip(manual_result, numpy_result)])
        print()

    print("test IFFT(FFT)")
    for i, case in enumerate(test_cases):
        print(len(case))
        print(f"case{i + 1}", case)
        manual_result = FFT(FFT(case, False), True)
        numpy_result = ifft(fft(case).tolist()).tolist()
        print("manual_result:", manual_result)
        print("numpy_result:", numpy_result)
        print("difference:", [i - j for i, j in zip(manual_result, numpy_result)])
        print()
