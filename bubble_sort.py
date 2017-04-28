
'''
bubble sort
'''

def bubble_sort(items):
    '''Bubble sort implementation, sorts items in incrementing order.'''
    items = list(items)
    swaped = False

    for _ in enumerate(items):
        for i, _ in enumerate(items[0:-1]):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                swaped = True
        if not swaped:
            break

    return items




if  __name__ == '__main__':
    unsorted_items = [5, 9, 3, 1, 2, 8, 4, 7, 6]
    sorted_items = bubble_sort(unsorted_items)

    print(unsorted_items)
    print(sorted_items)
    













































































