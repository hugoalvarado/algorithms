# http://www.geeksforgeeks.org/count-negative-numbers-in-a-column-wise-row-wise-sorted-matrix/

'''
Input:  M =  [-3, -2, -1,  1]
             [-2,  2,  3,  4]
             [4,   5,  7,  8]
Output : 4
We have 4 negative numbers in this matrix
'''

def count_matrix_negatives(matrix):
    return sum([count_negatives(row) for row in matrix])

def count_negatives(items):

    if len(items) == 0:
        return 0
    
    if len(items) == 1:
        return 0 if items[0] > 0 else 1

    mid = round(len(items)/2)

    if items[mid] < 0:
        return len(items[0:mid+1]) + count_negatives(items[mid+1:])
    else:
        return count_negatives(items[0:mid])


def count_matrix_negatives_diagonal(matrix):
    pass        


if __name__ == '__main__':
    a = [[-3, -2, -1,  1],
        [-2,  2,  3,  4],
        [4,   5,  7,  8]]
    #print(count_negatives(a[0]))  

    print(count_matrix_negatives(a))
    print(count_matrix_negatives_diagonal(a))
