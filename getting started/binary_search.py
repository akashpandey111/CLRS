def search(haystack, left, right, needle):
    mid = left + ((right - left) // 2)
    return mid if haystack[mid] == needle else search(haystack, left, mid - 1, needle) \
if haystack[mid] > needle else search(haystack, mid + 1, right, needle)

