"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

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

import rosegraphics as rg


def main():
    """Calls the other functions to demonstrate and/or test them."""
    two_circles()
    lines()
    circle_and_rectangle()
    run_test_plus_sign()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #     -- ANY two rg.Circle objects that meet the criteria are fine.
    #     -- File  COLORS.txt  lists all legal color-names.
    #   There is already a statement in   main   to test this function
    #    (by calling this function).
    #   HINT: Module  m2r_using_rosegraphics  has helpful examples for this.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()

    circle1 = rg.Circle(rg.Point(100, 50), 40)
    circle1.attach_to(window)

    circle2 = rg.Circle(rg.Point(175, 200), 80)
    circle2.fill_color = "cyan"
    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines, for the thicker Line):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #    -- ANY lines that meet the criteria are fine.
    #   There is already a statement in   main   to test this function
    #    (by calling this function).
    #   HINT: Module  m2r_using_rosegraphics  has helpful examples for this.
    #  ___
    #  IMPORTANT: Use the DOT TRICK to guess the name of the relevant method
    #    and instance variables.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()

    line1 = rg.Line(rg.Point(300, 20), rg.Point(50, 50))
    line1.attach_to(window)

    line2 = rg.Line(rg.Point(100, 100), rg.Point(121, 200))
    line2.thickness = 10
    line2.color = "red"
    line2.attach_to(window)

    midpoint = line2.get_midpoint()
    print(midpoint)
    print(midpoint.x)
    print(midpoint.y)

    window.render()
    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle (using its INSTANCE VARIABLES):
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.  (Hint: For this, you'll need to use
         a METHOD that begins with "get".)
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement this function, per its green doc-string above.
    #    -- ANY objects that meet the criteria are fine.
    #   There is already a statement in   main   to test this function
    #    (by calling this function).
    #   HINT: Module  m2r_using_rosegraphics  has helpful examples for this.
    #  ___
    #  IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()

    circle = rg.Circle(rg.Point(180, 115), 100)
    circle.fill_color = "blue"
    circle.attach_to(window)

    rectangle = rg.Rectangle(rg.Point(100, 250), rg.Point(25, 100))
    rectangle.attach_to(window)

    print(circle.outline_thickness)
    print(circle.fill_color)
    print(circle.center)
    print(circle.center.x)
    print(circle.center.y)

    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print(rectangle.get_center())
    print(rectangle.get_center().x)
    print(rectangle.get_center().y)

    window.render()
    window.close_on_mouse_click()


def run_test_plus_sign():
    """Tests the   plus_sign  function."""
    print()
    print("--------------------------------------------------")
    print("Testing the  plus_sign  function:")
    print("  See the graphics windows that pop up.")
    print("--------------------------------------------------")

    # TWO tests on ONE window.
    title = "Tests 1 & 2 of plus_sign"
    window = rg.RoseWindow(450, 250, title)

    circle = rg.Circle(rg.Point(100, 50), 30)
    circle.outline_color = "green"
    circle.fill_color = "blue"
    circle.outline_thickness = 10
    plus_sign(circle, "red", 5, window)  # Run the code to be tested
    window.continue_on_mouse_click()

    circle = rg.Circle(rg.Point(300, 100), 50)
    plus_sign(circle, "blue", 8, window)  # Run the code to be tested
    window.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = "Test 3 of plus_sign"
    window = rg.RoseWindow(400, 300, title)

    circle = rg.Circle(rg.Point(200, 150), 100)
    circle.outline_color = "yellow"
    circle.fill_color = "black"
    circle.outline_thickness = 7
    plus_sign(circle, "blue", 20, window)  # Run the code to be tested
    window.close_on_mouse_click()


def plus_sign(circle, color, thickness, window):
    """
    See   plus_sign_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- An rg.Circle.
      -- A color suitable for RoseGraphics.
      -- A positive integer suitable as a thickness.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      -- Draws the given rg.Circle on the given rg.RoseWindow
      -- Then draws an rg.Line from the leftmost point of the given rg.Circle
           to the rightmost point of the given rg.Circle,
           with color the given color and thickness the given thickness.
      -- Then draws an rg.Line from the topmost point of the given rg.Circle
           to the bottommost point of the given rg.Circle,
           with color the outline color of the given rg.Circle
           and thickness the outline thickness of the given rg.Circle.
      Must  render but ** NOT close **   the window.

    Type hints:
      :type circle:    rg.Circle
      :type color:     str
      :type thickness: int
      :type window:    rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------
    circle.attach_to(window)

    horizontal_line = rg.Line(
        rg.Point(circle.center.x - circle.radius, circle.center.y),
        rg.Point(circle.center.x + circle.radius, circle.center.y),
    )
    horizontal_line.color = color
    horizontal_line.thickness = thickness
    horizontal_line.attach_to(window)

    vertical_line = rg.Line(
        rg.Point(circle.center.x, circle.center.y - circle.radius),
        rg.Point(circle.center.x, circle.center.y + circle.radius),
    )
    vertical_line.color = circle.outline_color
    vertical_line.thickness = circle.outline_thickness
    vertical_line.attach_to(window)

    window.render()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# This unusual form is necessary for the special testing we provided.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
