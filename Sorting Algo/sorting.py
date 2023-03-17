class Sorting:
    arr = [1,4,5,2,10,20,6,7,8]
    
    
    def bubbleSort(arr):
        length = len(arr)
        
        for i in range(length):
            for j in range(0, length-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

            