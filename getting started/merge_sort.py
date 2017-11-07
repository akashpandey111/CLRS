def merge(array, p, q, r):
    a, b, i, j = array[p: q + 1], array[q + 1:], 0, 0
    for k in range(p, r):
        if a[i] <= b[j]:
            array[k] = a[i]
            i += 1
        else:
            array[k] = b[j]
            j += 1


def m_sort(array, p, q):
    if p < q:
        r = (p + q) // 2
        m_sort(array, p, r)
        m_sort(array, r + 1, q)
        merge(array, p, r, q)

a = [1, 3, 5, 2, 4, 6]

m_sort(a, 0, len(a) - 1)

print(a)
