#3. Answer for question - 3
num_list = [int(x) for x in input("Enter the sequence of comma separated numbers :\n").split(",")]
num_list = sorted(num_list)
print("The sorted list is :", num_list, "\n")
key = int(input("Enter the number to search for in the sorted list:\n"))
low = 0
flag = False
high = len(num_list) - 1

while low <= high:
  mid = (low + high)//2
  if(num_list[mid] == key):
    print("The number " + str(key) + " is found at index - " + str(mid) + " in the sorted list.")
    flag = True
    break
  elif(num_list[mid] < key):
    low = mid + 1
  else:
    high = mid - 1

if(flag == False):
    print("The number " + str(key) + " is not found in the given list/sorted list.")
