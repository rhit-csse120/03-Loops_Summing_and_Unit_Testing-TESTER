"""
This module demonstrates and practices:
  -- using ARGUMENTS in function CALLs,
  -- having PARAMETERS in function DEFINITIONS, and
  -- RETURNING a value from a function,
        possibly CAPTURING the RETURNED VALUE in a VARIABLE.
  -- UNIT TESTING.

Authors: David Mutchler, Rachel Krohn, Dave Fisher, Shawn Bohner, Sriram Mohan,
         Amanda Stouder, Vibha Alangar, Mark Hays, Dave Henthorn, Matt Boutell,
         Scott McClellan, Yiji Zhang, Mohammed Noureddine, Steve Chenoweth,
         Claude Anderson, Michael Wollowski, Chandan Rupakheti,
         Derek Whitley, Curt Clifton, Valerie Galluzzi, their colleagues and
         SOLUTION by David Mutchler.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

"""
Academic Integrity: I got help on this module from:
         PUT_HERE_THE_NAMES_OF_PEOPLE_WHO_HELPED_YOU_ON_THIS_MODULE_(IF_ANY).
"""  # DONE: If you got help from anyone on this module, list their names here.
import sys
import multiprocessing


COLOR_CODES = {
    "black": 20,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
}

TIMEOUT_SECONDS = 10


def run_tests(module_to_test):
    """Calls the   TEST   functions in this module."""
    passed, failed = 0, 0
    passed, failed = (passed, failed) + run_test_sum_of_digits(module_to_test)
    failed += run_test_digits_in_cube(module_to_test)
    failed += run_test_digits_in_power(module_to_test)
    failed += run_test_fancy_sums_of_digits(module_to_test)
    return failed


def run_test_sum_of_digits(module_to_test):
    """Tests the  sum_of_digits   function."""
    f = module_to_test.sum_of_digits
    tests_failed = 0
    tests_failed += run_test(f, [826], 16)
    tests_failed += run_test(f, [83135], 20)
    tests_failed += run_test(f, [2900], 11)
    tests_failed += run_test(f, [1000000], 1)
    return tests_failed


def run_test_digits_in_cube(module_to_test):
    """Tests the   digits_in_cube   function."""
    f = module_to_test.digits_in_cube
    tests_failed = 0
    tests_failed += run_test(f, [5], 8)
    tests_failed += run_test(f, [10000000000000], 1)
    tests_failed += run_test(f, [16], 19)
    tests_failed += run_test(f, [12], 18)
    tests_failed += run_test(f, [10000], 1)
    return tests_failed


def run_test_digits_in_power(module_to_test):
    """Tests the   digits_in_power   function."""
    f = module_to_test.digits_in_power
    tests_failed = 0
    tests_failed += run_test(f, [12, 3], 18)
    tests_failed += run_test(f, [16, 2], 13)
    tests_failed += run_test(f, [1234567890, 1], 45)
    tests_failed += run_test(f, [255, 3], 36)
    tests_failed += run_test(f, [2, 10], 7)
    tests_failed += run_test(f, [10000, 1], 1)
    return tests_failed


def run_test_fancy_sums_of_digits(module_to_test):
    """Tests the   fancy_sums_of_digits   function."""
    f = module_to_test.fancy_sums_of_digits
    tests_failed = 0
    tests_failed += run_test(f, [10], 1)
    tests_failed += run_test(f, [2], 19084)
    tests_failed += run_test(f, [35], 124309)
    tests_failed += run_test(f, [11], 76738)
    tests_failed += run_test(f, [10000], 1)
    return tests_failed


def run_test(function, arguments, expected_result):
    answer = run_with_timeout(function, arguments)
    if equals(answer, expected_result):
        return 0
    elif answer is None:
        print_colored(
            "Probably not yet implemented (returned None): " + function.__name__,
            color="green",
        )
        return 1
    else:
        print_colored(
            "{}({}) -> {}, expected {}".format(
                function.__name__, *arguments, answer, expected_result
            ),
            color="red",
        )
        return 1


def equals(actual, expected):
    PRECISION = 10
    if isinstance(expected, float):
        return round(actual, PRECISION) == round(expected, PRECISION)
    else:
        return actual == expected


def run_with_timeout(function, arguments):
    result_queue = multiprocessing.Queue()
    process = multiprocessing.Process(
        target=wrapper, args=(function, arguments, result_queue)
    )
    process.start()
    process.join(TIMEOUT_SECONDS)

    if process.is_alive():
        process.terminate()
        print_colored("killed", color="magenta")
        result = None
        process.join()
    else:
        result = result_queue.get()
    return result


def wrapper(function, arguments, result_queue):
    try:
        answer = function(*arguments)
        result_queue.put(answer)
    except Exception as e:
        print_colored("Exception: {}".format(e), color="cyan")
        result_queue.put(e)


def print_colored(*args, color="blue", flush=True, **kwargs):
    text = ""
    for arg in args:
        text = text + " " + str(arg)
    text = text.replace(" ", "", 1)
    sys.stdout.write("\033[%sm%s\033[0m" % (COLOR_CODES[color], text))
    print(**kwargs)
