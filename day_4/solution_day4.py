# DESCRIPTION:
'''
Write a function that takes a list comprised of other lists of integers and returns the sum of all numbers that appear in two or more lists in the input list. Now that might have sounded confusing, it isn't:

repeat_sum([[1, 2, 3],[2, 8, 9],[7, 123, 8]])
>>> sum of [2, 8]
return 10

repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]])
>>> sum of []
return 0

repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]])
sum of [1,8]
return 9
'''

# SOLUTION:
def repeat_sum(l):
    num_frequency = {}

    for sublist in l:
        unique_numbers = set(sublist)

        for x in unique_numbers:
            num_frequency[x] = num_frequency.get(x, 0) + 1

    result_sum = sum(x for x, freq in num_frequency.items() if freq >= 2)
    return result_sum