print("This is a binary search.")

arr = [-15,-12,3,24,57,69]
x = int(input("Enter a number to search from(-15, -12, 3, 24, 57, 69):"))

def binarysearch (arr,start,end,x):
    if end>=start:
        mid=start + (end+start)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarysearch(arr,start,mid-1,x)
        else:
            return binarysearch(arr,mid+1,end,x)
    else:
        return -1

result=binarysearch(arr,0,len(arr)-1,x)

if result != -1:
    print("Element found at index", int(result))
else:
    print("Element not found")
