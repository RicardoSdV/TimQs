from collections import deque


def tim_seq(low, high):
    res = []
    queue = deque(range(1, 10))

    while queue:
        n = queue.popleft()
        if n > high:
            continue
        if low <= n <= high:
            res.append(n)

        last = n % 10

        if last < 9:
            queue.append(n*10 + last+1)

    return res
