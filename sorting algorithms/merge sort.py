# tutorial link https://www.youtube.com/watch?v=_trEkEX_-2Q

def mergesort(arr):
    if(len(arr)>1):
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while(i<len(left) and j<len(right)):
            if(left[i] < right[j]):
                arr[k] = left[i]
                i=i+1
                k=k+1
            else:
                arr[k] = right[j]
                j=j+1
                k=k+1
        while i<len(left):
            arr[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            arr[k]=right[j]
            k=k+1
            j=j+1
arr=[10,2,11,3,43431,34,2343,3,43,413432,4,324,32432,332,342,4,32,43,432,5223543,24,32,432,4634243,5,435,43,5,324,32,5435,34,54,6,4,5,435,23,432,56,4,6,34543,4,543,65,4646,74576,7,657,67]
mergesort(arr)
print(arr)
