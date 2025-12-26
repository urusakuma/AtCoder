from typing import Callable


def meguru_bisect(lo: int, hi: int, f: Callable[[int], bool]):
    ''' 
    lo: 解になり得ない下限（False が保証される）\n
    hi: 解になり得ない上限（True が保証される）\n
    f(x) が True となる最小の整数 x を返す。
    '''
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if f(mid):
            hi = mid
        else:
            lo = mid
    return hi
