
class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        for i in range(n):
            for j in range(0,n-i-1):
                if arr[j]> arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr




if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr)
        for i in arr:
            print(i, end=' ')
        print()
