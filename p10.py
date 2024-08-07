#find the largest number in an array
def largest(arr,n):
    max=arr[0]
    
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
        return max

arr=[1,4,7,8,9]
n=len(arr)
Ans=largest(arr,n)
print("Largest in given array",Ans)