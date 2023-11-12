def reverse(num: int) -> int:
    neg = num < 0
    numstr = str(num)
    revstr = ''
    for i in range(len(numstr) -1, -1, -1):
        revstr = revstr + numstr[i]

    rev = int('-'+revstr) if neg else int(revstr)
    # any values between -2147483648 to +2147483648 (-+ 2**31)
    if (-2**31 > rev or rev > 2**31):
        return 0
    return rev

# print(reverse(1234))
# print(reverse(5678))
# print(reverse(1534236469))

