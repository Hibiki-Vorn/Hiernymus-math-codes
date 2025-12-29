from sage.all import *

def extended_gcd(a, b, x=None, y=None, count=1):
    if x is None:
        x = [1, 0]
    if y is None:
        y = [0, 1]

    r = a % b
    q = a // b
    x.append(x[count-1] - q*x[count])
    y.append(y[count-1] - q*y[count])
    
    if r == 0:
        # 最后一个非零余数的系数就是 gcd 的贝祖系数
        return (b, x[count], y[count])
    else:
        return extended_gcd(b, r, x, y, count+1)
