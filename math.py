def calc_amount0(liq, pa, pb):
    if pa > pb:
        pa, pb = pb, pa
    return liq * (pb - pa) / pa / pb


def calc_amount1(liq, pa, pb):
    if pa > pb:
        pa, pb = pb, pa
    return liq * (pb - pa)

from math import sqrt

liq = 1800 * 2
sqrtp_cur = sqrt(1800)

amount_in = 1800
price_diff = amount_in / liq
print(price_diff)
price_next = sqrtp_cur + price_diff
print(liq, price_next, sqrtp_cur, price_diff)
amount0 = calc_amount0(liq, price_next, sqrtp_cur)
amount1 = calc_amount1(liq, price_next, sqrtp_cur)
print(amount0, amount1)
# (amount0, amount1)
# > (998976618347425408, 5000000000000000000000)