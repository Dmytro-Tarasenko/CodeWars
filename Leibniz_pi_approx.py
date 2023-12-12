from math import pi, fabs

def iter_pi_my(epsilon: float) -> list:
    # pi/4 = 1 - 1/3 + 1/7 - 1/9 + 1/11 ...
    delta = 100
    sign = -1
    leibniz_pi = 0
    leibniz_sum = 1
    iter_num = 1
    while delta >= epsilon:
        leibniz_sum += sign/(2*iter_num+1)
        sign *= -1
        leibniz_pi = 4*leibniz_sum
        delta = fabs(leibniz_pi - pi)
        iter_num += 1
    return [iter_num, float(f'{leibniz_pi:.10f}')]


def iter_pi_ref(epsilon):
    pi_4 = 0
    k = 0
    while abs(pi_4 * 4 - pi) > epsilon:
        pi_4 += (-1) ** k / (k * 2 + 1)
        k += 1
    return [k, round(pi_4 * 4, 10)]

print(iter_pi_ref(0.0001))
