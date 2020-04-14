# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # If selected number is bigger than the on before it, swap it.
    # keep swapping the number untill the one before it is smaller, or it reaches 0
    for x in range(0,len(arr)):
        temp = arr[x]
        index = x
        while index > 0 and temp < arr[index-1]:
            arr[index] = arr[index-1]
            index -=1
            arr[index] = temp
        print(arr)
    return arr

# print(selection_sort([5,4,9,2]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    low = 0
    high = len(arr) - 1
    while low < high:
        for i in range(0,high):
            temp = arr[i+1]
            print(temp)
            if arr[i] > arr[i+1]:
                arr[i+1] = arr[i]
                arr[i] = temp
        high -=1
        
    return arr

#print(bubble_sort([2,4,6,3,5]))
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr