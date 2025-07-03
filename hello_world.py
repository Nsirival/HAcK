<<<<<<< HEAD
import math

def median(input):

  input.sort()

  listlen = len(my_list)
  midlist = listlen//2
  if listlen == 0:
    return ("list is empty")

  if listlen % 2 == 0:
    return((input[midlist-1] + input[midlist])/2)

  else:
    return(input[midlist])


my_list = [0, 3, 5, 7, 10, 11, 32, 87, 100, 999]
print(median(my_list))

=======
def mean(input):
  sum = 0
  for entry in input:
    sum += entry
  return sum / len(input)

my_list = [0, 1, 2, 3, 4, 5]
print(mean(my_list))
>>>>>>> mean_branch
