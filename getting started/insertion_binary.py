def search(arr, left, right, needle):
    if left == right:
        return left if arr[left] > needle else left + 1
    elif left > right:
        return left
    else:
        mid = (left + right) // 2
        return search(arr, mid + 1, right, needle) if arr[mid] < needle \
    else search(arr, left, mid - 1, needle) if arr[mid] > needle else mid


def insertion_sort(array):
    for index in range(1, len(array)):
        ind = search(array, 0, index - 1, array[index])
        array = array[:ind] + [array[index]] + array[ind: index] + array[index + 1:]
    return array


if __name__ == '__main__':
    print(insertion_sort(array=list(map(int, input().strip().split(' ')))))
