def insertion_sort(array, n):
    if n > 1:
        insertion_sort(array, n - 1)
        key, j = array[n - 1], n - 2
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


if __name__ == '__main__':
    array = list(map(int, input().strip().split(' ')))
    insertion_sort(array=array, n=len(array))
    print(array)
