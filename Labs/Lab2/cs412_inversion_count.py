"""
name: Cameron Hakenson
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


def mergesort(arr):
    if len(arr) > 1:
        # Get the mid point
        m = len(arr) // 2

        # Get the left and right halves
        left, right = arr[:m], arr[m:]

        # sort the left and right halves
        invertions = mergesort(left)
        invertions += mergesort(right)

        # Copy the sorted left and right halves back to arr.
        for i in range(m):
            arr[i] = left[i]
        for j in range(m, len(arr)):
            arr[j] = right[j - m]

        # Run the merge operation on arr
        invertions += merge(arr, m)
        return invertions
    else:
        return 0


def merge(arr, m):
    invertions = 0
    i, j = 0, m
    n = len(arr)
    B = [0 for _ in range(n)]
    for k in range(n):
        if j >= n:
            B[k] = arr[i]
            i += 1
        elif i >= m:
            B[k] = arr[j]
            j += 1
        elif arr[i] <= arr[j]:
            B[k] = arr[i]
            i += 1
        else:
            invertions += m - i
            B[k] = arr[j]
            j += 1
    for k in range(n):
        arr[k] = B[k]

    return invertions


def main():
    arr_input = input()
    arr_split = arr_input.split(" ")
    arr = []
    for num in arr_split:
        arr.append(int(num))
    print(mergesort(arr))


if __name__ == "__main__":
    main()
