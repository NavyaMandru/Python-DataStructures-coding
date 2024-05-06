# Insertion sort algorithm

"""
works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list.

Time Complexity : O(N^2)

Space Complexity : O(1)

"""

def insertion_sort(arry, n):

  for i in range(1,n):
    key = arry[i]
    j = i-1

    while j>=0 and arry[j] > key:
      arry[j+1] = arry[j]
      j -= 1
    arry[j+1] = key
  
  return arry

if __name__ == "__main__":
    arry = list()
    n = int(input("enter no.of elements: "))

    # get the elements from user and append elements to the list
    for i in range(n):
        arry.append(int(input()))

    # function call
    sorted_array = insertion_sort(arry, n)

    print("sorted array :",sorted_array)


