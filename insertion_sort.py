
'''
Insertion Sort
'''

def insertion_sort(items):
    '''Insertion sort implementation, sorts items in incrementing order.'''
    items = list(items)

    for i, _ in enumerate(items[0:-1]):
        next_i = i+1
        if items[next_i] < items[i]:
            #find insertion point in already sorted section
            for j, v in enumerate(items[0:next_i]):
                if items[next_i] < items[j]:
                    items.insert(j, items[next_i])
                    items.pop(next_i + 1 )
                    break

    return items


if  __name__ == '__main__':
    unsorted_items = [5, 9, 3, 1, 2, 8, 4, 7, 6, 4]    
    sorted_items = insertion_sort(unsorted_items)

    print('--')
    print(unsorted_items)
    print(sorted_items)







































































