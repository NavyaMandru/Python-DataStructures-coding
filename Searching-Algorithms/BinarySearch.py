# Binary Search

"""Binary Search Algorithm is used in a sorted array by repeatedly dividing the search interval in half. 
The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 

"""

def BinarySearch(arry, x, n):

low = 0
high = n

while(low <= high):
  mid = low + (high - low) //2

  if arry[mid] == x:
    return mid
  elif arry[mid] < x:
    low = mid + 1
  else:
    high = mid - 1

return -1

if name == "__main__":
  arru = list()
  
  finding_element = int(input("enter the element that you want to find in the list: "))
  
  n = int(input("enter no.of elements: "))

  # get the elemets from user and append elements to the list
  for i in range(n):
    arry.append(int(input()))

  # sort arry
  arry = sorted(arry)

  # functtion call
  result = BinarySearch(arry,finding_element,n)

  if (result == -1):
    print("Element not present in the list")
  else:
    print("Element present the the index ", result)
  
