from random import randint
from timeit import repeat
from bubble_sort import bubblesort
from quick_sort import quicksort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from timsort import timsort

def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")

    

if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    ARRAY_LENGTH = 1000
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # Call the function using the name of the sorting algorithm
    # and the array you just created
    print("\n")
    run_sorting_algorithm(algorithm="sorted", array=array)
    run_sorting_algorithm(algorithm="bubblesort", array=array)
    run_sorting_algorithm(algorithm="quicksort", array=array)
    run_sorting_algorithm(algorithm="insertion_sort", array=array)
    run_sorting_algorithm(algorithm="merge_sort", array=array)
    run_sorting_algorithm(algorithm="timsort", array=array)
