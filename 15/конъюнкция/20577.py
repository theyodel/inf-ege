# 20577

"""
Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n. Определите наибольшее натуральное число A, такое что выражение
                                        (x & A ≠ 0) → ((x & 698 = 0) → (x & 321 ≠ 0))
                тождественно истинно (то есть принимает значение 1 при любом натуральном значении переменной x)?
"""

def f(x):
    return( (x & a != 0) <= ((x & 698 == 0) <= (x & 321 != 0)) )

for a in reversed(range(1,10000)):
    if all(f(x) for x in range(1,10000)):
        print(a)
        break

# Ответ: 1019