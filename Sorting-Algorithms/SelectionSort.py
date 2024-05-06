# Selection sort algorithm

"""
repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.

Time Complexity: O(N^2)

Space Complexity: O(1)

"""
def selection_sort(arry, n):

  for i in range(n):
    for j in range(i+1, n):
      if arry[i] > arry[j]:
        arry[i], arry[j] = arry[j], arry[i]

  return arry

if __name__ == "__main__":
    arry = list()
    n = int(input("enter no.of elements: "))

    # get the elements from user and append elements to the list
    for i in range(n):
        arry.append(int(input()))

    # function call
    sorted_array = selection_sort(arry, n)

    print("sorted array :",sorted_array)

