
'''
selection sort
'''

def selection_sort(items):
    '''Selection sort implementation, sorts items in incrementing order.'''
    items = list(items)

    for i, v in enumerate(items):
        
        smallest_index = find_smallest(items, i)

        if items[smallest_index] < v:
            items[i], items[smallest_index] = items[smallest_index] , items[i]
        
    return items


def find_smallest(items, start):
    '''Find the position of the smallest value.'''
    smallest = items[start]
    index = 0

    #could use min()

    for i, v in enumerate(items[start:]):
        if v < smallest:
            smallest = v
            index = i

    return index + start


if  __name__ == '__main__':
    unsorted_items = [5, 9, 3, 1, 2, 8, 4, 7, 6, 4]
    sorted_items = selection_sort(unsorted_items)

    print(unsorted_items)
    print(sorted_items)







































































