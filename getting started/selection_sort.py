array = list(map(float, input("Array >>> ").strip().split(' ')))

for index, item in enumerate(array):
    min_item = min(array[index:])
    min_index = array.index(min_item)
    array[index], array[min_index] = array[min_index], array[index]

print(array, flush=True)
