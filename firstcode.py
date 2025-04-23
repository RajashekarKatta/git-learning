# this is my first python code
print("Hello World!..")
print("Katta Rajashekar")
# the above statement prints "Hello World"

def smallestMissingPositive(arr):
    n = len(arr)

    # Step 1: Place each number in its right index if possible
    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i]-1] != arr[i]:
            correct_idx = arr[i] - 1
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]

    # Step 2: Find the first index where value is not index+1
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    # If all are in place, smallest missing is n+1
    return n + 1
print(smallestMissingPositive([3, 4, -1, 1]))     # Output: 2

