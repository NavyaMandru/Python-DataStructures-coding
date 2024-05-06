# Linear search algorithm

""" starts at one end and goes through each element of a list until the desired element is found, 
otherwise the search continues till the end of the data set.

Time Complexity:

Best case - O(1)
worst case - O(N) where N is sie of array

Space Complexity: O(1) as except for the variable to iterate through the list, no other variable is used. 
"""


def linear_search(arry, x, n):
    for i in range(n):
        if arry[i] == x:
            return i
    return -1


if __name__ == "__main__":
    arry = list()

    finding_element = int(input("enter the element that you want to find in the list: "))

    n = int(input("enter no.of elements: "))

    # get the elements from user and append elements to the list
    for i in range(n):
        arry.append(int(input()))

    # function call
    result = linear_search(arry, finding_element, n)

    if result == -1:
        print("Element not present in the list")
    else:
        print("Element present the the index ", result)
        
    

