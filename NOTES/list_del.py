
# clist = ['Purple', 'Blue', 'Green', 'Pink', 'Red']
# print(clist)
# print("**************************************")
#
# print( clist[3] )
#
# del clist[3]
# print(clist)
#
# print("**************************************")
#
# del clist[2]
# print(clist)
# nlist = [11,45,76,2,8 ]
# r=sorted(nlist,reverse=True)
# print(list(r))
# print(r[len(r)-2])
#
# Bubble sort in Python

# Bubble sort in Python

def bubbleSort(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                # temp = array[j]
                # array[j] = array[j + 1]
                # array[j + 1] = temp
                array[j],array[j+1]=array[j+1], array[j]

data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)