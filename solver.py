#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0] * len(items)

    dp = [[0] * (capacity + 1) for _ in range(item_count + 1)]
    for i in range(1):
        dp[0][i] = 0

    for i in range(1, len(dp)):
        for j in range(len(dp[0])):

            curr_val = items[i - 1].value
            curr_weight = items[i - 1].weight

            not_selected = dp[i - 1][j]
            if j - curr_weight < 0:
                selected = 0
            else:
                selected = dp[i - 1][j - curr_weight] + curr_val
            dp[i][j] = max(selected, not_selected)

    curr_i = - 1
    curr_j = -1
    for i in range(item_count):
        curr = dp[curr_i][curr_j]
        not_taken = dp[curr_i - 1][curr_j]

        if curr == not_taken:
            taken[-1 - i] = 0
            curr_i -= 1
        else:
            taken[-1 - i] = 1
            curr_i -= 1
            curr_j -= items[-1 - i].weight

    # prepare the solution in the specified output format
    output_data = str(dp[-1][-1]) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py '
              './data/ks_4_0)')
