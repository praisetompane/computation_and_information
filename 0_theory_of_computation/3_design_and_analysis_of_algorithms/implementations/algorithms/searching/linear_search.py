def linear_search(value, arr):
    i = 0
    upperBound = len(arr) - 1
    while i <= upperBound:
        if value == arr[i]:
            return i
        i = i + 1
    return None


###Test
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(linear_search(8, data))
