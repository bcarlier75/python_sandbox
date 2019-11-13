def pal_str(st):
    if st == st[::-1]:
        print("The string is a palindrome")
    else:
        print("Not a palindrome")


def pal_list(arr):
    for i in range(0, int(len(arr) / 2)):
        if arr[i] != arr[len(arr) - 1 - i]:
            print("Not a palindrome")
            return
    print("The array is a palindrome")


arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
pal_list(arr)
test = 12321
st = str(test)
pal_str(st)
st = 'racecar'
pal_str(st)


