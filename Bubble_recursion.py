class Solution:

    def bubbleSort(self,arr,n=None):
        if n is None:
            n = len(arr)
        if n ==1:
            return
        
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        
        return self.bubbleSort(arr,n-1)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr)
        for i in arr:
            print(i, end=' ')
        print()

