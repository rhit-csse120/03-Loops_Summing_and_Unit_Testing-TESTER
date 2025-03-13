"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

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

###############################################################################
# DONE: 2. Read the following, then change its _TODO_ to DONE.
#   Throughout these exercises, you must use  RANGE  statements.
#   At this point of the course, you are restricted to the SINGLE-ARGUMENT
#   form of RANGE statements, like this:
#      range(blah):
#   There is a MULTIPLE-ARGUMENT form of RANGE statements (e.g. range(a, b))
#   but you are NOT permitted to use the MULTIPLE-ARGUMENT form yet,
#   for pedagogical reasons.
###############################################################################
import math


def main():
    """Calls the   TEST   functions in this module."""
    run_test_sum_cosines()
    run_test_sum_square_roots()


def run_test_sum_cosines():
    """Tests the   sum_cosines   function."""
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #  ___
    #  Use the same 4-step process as in implementing previous
    #  TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   sum_cosines   function:")
    print("--------------------------------------------------")

    # Test 1:
    expected = 0.13416
    answer = sum_cosines(3)
    print("Test 1 expected:", expected)
    print("       actual:  ", answer)

    # Test 2:
    expected = 1
    answer = sum_cosines(0)
    print("Test 2 expected:", expected)
    print("       actual:  ", answer)

    # Test 3:
    expected = math.cos(0) + math.cos(1) + math.cos(2)
    answer = sum_cosines(2)
    print("Test 3 expected:", expected)
    print("       actual:  ", answer)


def sum_cosines(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  Returns the sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
    Type hints:
      :type n: int
      :rtype: float
    """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-FIRST DEVELOPMENT (TFD).
    #  ___
    #  No fair running the code of  sum_cosines  to GENERATE
    #  test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------
    total = 0
    for k in range(n + 1):
        total = total + math.cos(k)
    return total


def run_test_sum_square_roots():
    """Tests the   sum_square_roots   function."""
    # -------------------------------------------------------------------------
    # DONE: 5. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #  ___
    #  Use the same 4-step process as in implementing previous
    #  TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   sum_square_roots   function:")
    print("--------------------------------------------------")

    # Test 1:
    expected = 11.854408
    answer = sum_square_roots(5)
    print("Test 1 expected:", expected)
    print("       actual:  ", answer)

    # Test 2:
    expected = 0
    answer = sum_square_roots(0)
    print("Test 2 expected:", expected)
    print("       actual:  ", answer)

    # Test 3:
    expected = 1.41421356237  # approximately
    answer = sum_square_roots(1)
    print("Test 3 expected:", expected)
    print("       actual:  ", answer)


def sum_square_roots(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  Returns the sum of the square roots of the integers
       2, 4, 6, 8, ... 2n    inclusive, for the given n.
           So if n is 7, the last term of the sum is
           the square root of 14 (not 7).
    Side effects:   None.
    Example:
      If n is 5, this function returns
         sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
      which is about 11.854408.
    Type hints:
      :type n: int
      :rtype: float
    """
    # -------------------------------------------------------------------------
    # DONE: 6. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-FIRST DEVELOPMENT (TFD).
    #  ___
    #  No fair running the code of  sum_square_roots  to GENERATE
    #  test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------
    total = 0
    for k in range(n):
        total = total + math.sqrt((2 * k) + 2)
    return total


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# This unusual form is necessary for the special testing we provided.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
