class Solution:
    def mergeSort(self,arr,l,r):
        if l<r:
            mid = (l+r)//2
            self.mergeSort(arr,l,mid+1)
            self.mergeSort(arr,mid+1,r)
            self.merge(arr,l,mid,r)

    def merge(self,arr, l,mid,r):
        left = arr[l:mid+1]
        right = arr[mid+1:r+1]

        i,j,k=0,0,l

        while i< len(left) and j< len(right):
            if left[i]<right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i< len(left):
            arr[k] = left[i]
            i+=1
            k += 1
        while j< len(right):
            arr[k] = right[j]
            j+=1 
            k += 1


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.mergeSort(arr,0,len(arr)-1)
        print(*arr)
        print("~")
        t -= 1

    
