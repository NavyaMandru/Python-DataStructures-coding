# Bubble sort algorithm

"""
Bubble sort algorithm works by repeatedly swapping the adjacent elements if they are in the wrong order.

Time Complexity: O(N^2)

Space Complexity: O(1)

"""
def bubble_sort(arry, n):
  swap = False

  for i in range(n):
    swap = False
    
    for j in range(0, n-i-1):
      if arry[j] > arry[j+1]:
        arry[j], arry[j+1] = arry[j+1], arry[j]
        swap = True
    if swap == False:
      break

  return arry

if __name__ == "__main__":
    arry = list()
    n = int(input("enter no.of elements: "))

    # get the elements from user and append elements to the list
    for i in range(n):
        arry.append(int(input()))

    # function call
    sorted_array = bubble_sort(arry, n)

    print("sorted array :",sorted_array)
