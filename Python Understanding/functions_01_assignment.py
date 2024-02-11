print("NAME:: RAYAN AHMED")
print("ROLL NO:: BITF20M535")

print("\n ***ASSIGNMENT FUNCTIONS (BINARY SEARCH)***\n")


def binarySearch(List1, key, n):
    low = 0
    high = n-1
    mid = 0

    while(low <= high):
        mid = low + (high-low)//2

        if(key == List1[mid]):
            return mid
        elif(key < List1[mid]):
            high = mid-1
        else:
            low = mid+1
        
    return -1



Array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\n...Calling Binary Search Function...")

key = binarySearch(Array, 5, 10)

if(key >= 0):
    print("Key Successfully found at index: ", key)
else:
    print("SORRY! Key Not found...")

print("\n%%Thankyou%%")
