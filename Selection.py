class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n-1):
            min_index = i
            for j in range(i+1,n):
                if arr[j]< arr[min_index]:
                    min_index = j
            arr[i],arr[min_index] = arr[min_index], arr[i]
        
        return arr




class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = [int(i) for i in input().split()]

        obj = Solution()
        obj.selectionSort(arr)

        IntArray().Print(arr)
        print("~")