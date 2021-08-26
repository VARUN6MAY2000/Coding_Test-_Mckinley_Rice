def MinMax(arr, n):
    a1=arr[0]
    a2=arr[0]
    for i in range(1,n):
        if a1<arr[i]:
            a1=arr[i]
        if a2>arr[i]:
            a2=arr[i]
    return a1,a2

# Driver Program
print("Give the space seprated values of array -")
arr = input().split()
n = len(arr)
a=MinMax(arr,n)
print ("Minimum element of array: ",a[0],"\nMaximum elemnt of array: ",a[1])
