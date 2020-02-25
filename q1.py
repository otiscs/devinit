# import pdb
# pdb.set_trace()

'''
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged. The input list is not necessarily ordered in any way.
For example, 
given         [(1, 3), (*5, 12), (4, *10), (20, 25)], you 
should return [(1, 3), (4, 12), (20, 25)].

Input:        disordered list of overlapping intervals.
Output:       list of 1 or more pairs of intervals with overlapping intervals merged.
Edge cases:   when list length has finished?
Aassumptions: 
              the list is disordered
              the list lengh is arbitary, needs to loop over any length
              if all data is overlapping
'''
abstr = [ (6, 8), (2,8), (2, 4), (4, 7) ]
testData = [(1, 3), (5, 12), (4, 10), (20, 25)]

data = []
def merge(numbers):
  for number in numbers:
    data.append((number[0], 0))
    data.append((number[1], 1))
  data.sort()
  
  # init open list
  merged = []

  dataList = [data[0]]
  # loop over the data applying a 1 or 0 depending on if upper or loewr bound.
  for i in range(1, len(data)):
    num = data[i]
    if num[1] == 0:
          # lower bound so .append
        dataList.append(num)
    elif num[1] == 1:
          #then an upper bound so .pop()
        if dataList:
	        first = dataList.pop()
        if len(dataList) == 0:
	        merged.append( (first[0], num[0]))
          # merged results
  return merged



