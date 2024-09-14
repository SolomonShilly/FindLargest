def search(list):
  temp = 0
  for x in list:
    if temp <= x:
      largestValue = x
      temp = largestValue
  return largestValue

list = [1, 300, 2, 3, 4, 100, 5, 6, 60, 95, 30, 1000, 39, 1, 0, -1, 34, 28, 2991, 3940, 1]
search(list)
