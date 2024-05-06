# Binary Search

"""Binary Search Algorithm is used in a sorted array by repeatedly dividing the search interval in half. 
The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 

Time Complexity:
Best case - O(1)
Worst Case: O(log N)
Avarage Case: O(log N)

Space Complexity: O(1)

"""

def binary_search(arry, x, n):
    low = 0
    high = n

    while low <= high:
        mid = low + (high - low) // 2

        # check if x, if present at mid
        if arry[mid] == x:
            return mid
        # If x if greater, ignore left
        elif arry[mid] < x:
            low = mid + 1
        # If x if smaller, ignore right
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    arry = list()

    finding_element = int(input("enter the element that you want to find in the list: "))

    n = int(input("enter no.of elements: "))

    # get the elements from user and append elements to the list
    for i in range(n):
        arry.append(int(input()))

    # sort arry
    arry = sorted(arry)

    # function call
    result = binary_search(arry, finding_element, n)

    if result == -1:
        print("Element not present in the list")
    else:
        print("Element present the the index ", result)

