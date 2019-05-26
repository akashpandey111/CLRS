import sys


def maximum_crossing_sub_array(arr, low, mid, high):
    left_sum, right_sum, s, max_left, max_right = -sys.maxsize - 1, -sys.maxsize - 1, 0, -1, -1

    for i in range(mid, low, -1):
        s += arr[i]
        if s > left_sum:
            left_sum = s
            max_left = i

    s = 0

    for i in range(mid + 1, high + 1):
        s += arr[i]
        if s > right_sum:
            right_sum = s
            max_right = i

    return max_left, max_right, left_sum + right_sum


def maximum_sub_array_recursive(arr, low, high):
    if low == high:
        return low, high, arr[low]  # one element only
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = maximum_sub_array_recursive(arr, low, mid)
        right_low, right_high, right_sum = maximum_sub_array_recursive(arr, mid + 1, high)
        cross_low, cross_high, cross_sum = maximum_crossing_sub_array(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


if __name__ == '__main__':
    a = [9, -1, 0, -43, 22, 100]

    recursive = maximum_sub_array_recursive(a, 0, len(a) - 1)

    print(recursive)
