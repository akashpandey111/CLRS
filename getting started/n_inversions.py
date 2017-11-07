def merge(array, p, q, r):
    a, b, i, j, inverse = array[p: q + 1], array[q + 1:], 0, 0, 0
    while i + j < r:
        try:
            if a[i] <= b[j]:
                i += 1
            else:
                j += 1
                inverse += (r - i)
        except IndexError:
            break
    return inverse


def m_sort(array, p, q):
    inverse = 0
    if p < q:
        r = p + ((q - p) // 2)
        inverse += m_sort(array, p, r) + m_sort(array, r + 1, q) + merge(array, p, r, q)
    return inverse


a = [1, 6, 2, 5, 3, 4, 0]
a = m_sort(a, 0, len(a) - 1)
print(a)
