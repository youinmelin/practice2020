import numpy

list_with_dupes = [1, 5, 6, 2, 5, 6, 8, 3, 8, 3, 3, 9, 7]
# find the unique data from list, return the unique data list and the index list
print(numpy.unique(list_with_dupes, return_index=True))



