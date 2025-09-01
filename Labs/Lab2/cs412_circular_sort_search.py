"""
name: Cameron Hakenson
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


# searches for a certain key in a circular sorted array
def circular_binary_search(arr, low, high, key):

    # handles not finding the value
    if high < low:
        return -1

    # determines the mid value
    mid = (low + high) // 2

    # determines if the mid value is key
    if key == arr[mid]:
        return mid

    if arr[low] <= arr[mid]:
        if (key >= arr[low]) and (key < arr[mid]):
            return circular_binary_search(arr, low, (mid - 1), key)
        else:
            return circular_binary_search(arr, (mid + 1), high, key)
    else:
        if (key > arr[mid]) and (key <= arr[high]):
            return circular_binary_search(arr, (mid + 1), high, key)
        else:
            return circular_binary_search(arr, low, (mid - 1), key)


def main():
    # takes in the input string and turns it into an array of integers
    arr_input = input()
    arr_split = arr_input.split(" ")
    arr = []
    for num in arr_split:
        arr.append(int(num))
    key = int(input())

    # performs the circular search
    print(circular_binary_search(arr, 0, len(arr) - 1, key))


if __name__ == "__main__":
    main()
