import random
import time


def sequential_search(alist, item):
    start_time = time.time()
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    end_time = time.time()
    execution_time = end_time - start_time
    return found, execution_time


def ordered_sequential_search(alist, item):
    start_time = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    end_time = time.time()
    execution_time = end_time - start_time
    return found, execution_time


def binary_search_iterative(alist, item):
    start_time = time.time()
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end_time = time.time()
    execution_time = end_time - start_time
    return found, execution_time


def binary_search_recursive(alist, item):
    start_time = time.time()
    if len(alist) == 0:
        found = False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                found, _ = binary_search_recursive(alist[:midpoint], item)
            else:
                found, _ = binary_search_recursive(alist[midpoint + 1 :], item)
    end_time = time.time()
    execution_time = end_time - start_time
    return found, execution_time


def main():
    num_list = 100
    list_sizes = [500, 1000, 10000]
    target = -1

    for size in list_sizes:
        total_time_sequential_search = 0
        total_time_ordered_sequential_search = 0
        total_time_binary_search_iterative = 0
        total_time_binary_search_recursive = 0

        for _ in range(num_list):
            random_list = [random.randint(1, 10000) for _ in range(size)]
            random_list.sort()

            found, time_sequential_search = sequential_search(random_list, target)
            total_time_sequential_search += time_sequential_search

            found, time_ordered_sequential_search = ordered_sequential_search(
                random_list, target
            )
            total_time_ordered_sequential_search += time_ordered_sequential_search

            found, time_binary_search_iterative = binary_search_iterative(
                random_list, target
            )
            total_time_binary_search_iterative += time_binary_search_iterative

            found, time_binary_search_recursive = binary_search_recursive(
                random_list, target
            )
            total_time_binary_search_recursive += time_binary_search_recursive

        avg_sequential_search = total_time_sequential_search / num_list
        avg_ordered_sequential_search = total_time_ordered_sequential_search / num_list
        avg_binary_search_iterative = total_time_binary_search_iterative / num_list
        avg_binary_search_recursive = total_time_binary_search_recursive / num_list

        print(f"List size: {size}")
        print(f"Sequential Search took {avg_sequential_search:.7f} seconds to run on average")
        print(
            f"Ordered Sequential Search took {avg_ordered_sequential_search:.7f} seconds to run on average"
        )
        print(
            f"Binary Search took {avg_binary_search_iterative:.7f} seconds to run on average"
        )
        print(
            f"Binary Search (Recursive) took {avg_binary_search_recursive:.7f} seconds to run on average"
        )
        print()


if __name__ == "__main__":
    main()
