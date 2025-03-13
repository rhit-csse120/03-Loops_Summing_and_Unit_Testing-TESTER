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


def main():
    """Calls the   TEST   functions in this module."""
    run_test_sum_powers()
    run_test_sum_powers_in_range()


def run_test_sum_powers():
    """Tests the   sum_powers   function."""
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function.
    #   It TESTS the  sum_powers  function defined below.
    #   Include at least **   3   ** tests.
    #  ___
    #  Use the same 4-step process as in implementing previous
    #  TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   sum_powers   function:")
    print("--------------------------------------------------")

    # Test 1:
    expected = 3.80826
    answer = sum_powers(5, -0.3)
    print("Test 1 expected:", expected)
    print("       actual:  ", answer)

    # Test 2:
    expected = 144.45655
    answer = sum_powers(100, 0.1)
    print("Test 2 expected:", expected)
    print("       actual:  ", answer)

    # Test 3:
    expected = 250 * 501
    answer = sum_powers(500, 1)
    print("Test 3 expected:", expected)
    print("       actual:  ", answer)


def sum_powers(n, p):
    """
    What comes in:  A non-negative integer n
                    and a number p.
    What goes out:  Returns the sum   1**p + 2**p + 3**p + ... + n**p
       for the given numbers n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:   None.
    Examples:
      -- sum_powers(5, -0.3) returns about 3.80826
      -- sum_powers(100, 0.1) returns about 144.45655
    Type hints:
      :type n: int
      :type p: int | float
      :rtype: int | float
    """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   ___
    #   No fair running the code of  sum_powers  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------
    total = 0
    for k in range(n):
        total = total + (k + 1) ** p
    return total


def run_test_sum_powers_in_range():
    """Tests the   sum_powers_in_range   function."""
    # -------------------------------------------------------------------------
    # TODO: 5. Implement this function.
    #   It TESTS the  sum_powers_in_range  function defined below.
    #   Include at least **   3   ** tests.
    #  ___
    #  Use the same 4-step process as in implementing previous
    #  TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    print()
    print("--------------------------------------------------")
    print("Testing the   sum_powers_in_range   function:")
    print("--------------------------------------------------")

    # Test 1:
    expected = 142.384776
    answer = sum_powers_in_range(3, 100, 0.1)
    print("Test 1 expected:", expected)
    print("       actual:  ", answer)

    # Test 2:
    expected = 144.45655
    answer = sum_powers_in_range(1, 100, 0.1)
    print("Test 2 expected:", expected)
    print("       actual:  ", answer)

    # Test 3:
    expected = 5 + 6 + 7
    answer = sum_powers_in_range(5, 7, 1)
    print("Test 3 expected:", expected)
    print("       actual:  ", answer)


def sum_powers_in_range(m, n, p):
    """
    What comes in:  Non-negative integers m and n, with n >= m,
                    and a number p.
    What goes out:  Returns the sum
           m**p + (m+1)**p + (m+2)**p + ... + n**p
       for the given numbers m, n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:  None.
    Example:
      -- sum_powers_in_range(3, 100, 0.1) returns about 142.384776
    Type hints:
      :type m: int
      :type n: int
      :type p: int | float
      :rtype: int | float
    """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #  ___
    #  No fair running the code of  sum_powers_in_range  to GENERATE
    #  test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------
    total = 0
    for k in range(n - m + 1):
        total = total + (k + m) ** p
    return total


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# This unusual form is necessary for the special testing we provided.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
