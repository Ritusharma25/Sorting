class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        
        for i in range(1, n):
            j = i
            while arr[j-1]>arr[j] and j>0:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                j-=1
        return arr
            




if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.insertionSort(arr)
        print(*arr)
        print("~")
        t -= 1
