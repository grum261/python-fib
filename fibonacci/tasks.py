from celery import shared_task


@shared_task
def fibonacci_seq(n: int) -> list:
    sequence = []
    for i in range(n):
        sequence.append(str(_fibonacci_doubling(i)[0]))

    return sequence


def _fibonacci_doubling(n: int) -> tuple:
    if n == 0:
        return 0, 1
    else:
        a, b = _fibonacci_doubling(n >> 1)
        c = a * ((b << 1) - a)
        d = a * a + b * b
        if n & 1:
            return d, c + d
        else:
            return c, d
