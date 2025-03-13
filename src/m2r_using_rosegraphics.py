"""
This module uses ROSEGRAPHICS to demonstrate:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES.

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
# DONE: 2.
#   RUN this program.  Then answer the following, FOLLOWING YOUR INSTRUCTOR
#     and GETTING HELP AS NEED! (Ask questions!!!)
#  _
#     a. For the RoseGraphics coordinate system:
#  _
#        -- Where is the (0, 0) point on the screen?
#              Upper-left corner.
#  _
#        -- In what direction on the screen does the positive X-axis point?
#              To the right.
#  _
#        -- In what direction on the screen does the positive Y-axis point?
#              Down.
#  _
#     b. Write a line of code that constructs a RoseWindow object:
#            window = rg.RoseWindow()
#
#     c. What is the default height of a RoseWindow?
#        (Select RoseWindow in the code below, then  View ~ Quick Documentation
#         to determine the answer to this question.)
#            300
#  +
#     d. Write a line of code that construct a RoseWindow object
#        whose height is 100:
#        (Use the   View ~ Quick Documentation   trick to figure it out)
#            window = rg.RoseWindow(height=100)
#  +
#     e. Use the DOT trick to answer the following:
#  +
#          -- Write the names of two types of graphics objects that
#             you can construct OTHER than Circle and Point:
#                Square, Rectangle.
#  +
#          -- Write the names of three METHODs that Circle objects have:
#                attach_to, move_by, move_center_to, ...
#  +
#          -- Write the names of three INSTANCE VARIABLEs that Circle
#             objects have:
#                radius, center, outline_color, outline_thickness, ...
#  _
#     f. What does a RoseWindow RENDER method do?
#            Plops onto the screen all the graphical objects that have
#            been attached to the RoseWindow.
#  _
#     g. When is a RoseWindow close_on_mouse_click method call
#        necessary?  Why?
#            It is necessary after all drawing is done.
#            Without it, the window goes away when the code completes executing.
#            With it, the code pauses with the window open for the user
#            to see the drawing that was done in the RoseWindow.
#  _
#   ASK QUESTIONS ** NOW ** if you do not understand how the
#     RoseGraphics graphics system works.
#  _
#   When you are confident that you have written correct answers
#   to the above questions (ASK QUESTIONS AS NEEDED!),
#   change the above _TODO_ to DONE.
###############################################################################

import rosegraphics as rg


def main():
    """
    Uses ROSEGRAPHICS to demonstrate:
      -- CONSTRUCTING objects,
      -- applying METHODS to them, and
      -- accessing their DATA via INSTANCE VARIABLES
    """
    example1()
    example2()
    example3()


def example1():
    """Displays an empty window."""
    window = rg.RoseWindow(500, 300, "Example 1: An empty window")
    window.close_on_mouse_click()


def example2():
    """Displays two Point objects."""
    # -------------------------------------------------------------------------
    # Construct the window in which objects will be drawn.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()

    # -------------------------------------------------------------------------
    # Construct some rg.Point objects.
    # Note: the y-axis goes DOWN from the TOP.
    # -------------------------------------------------------------------------
    point1 = rg.Point(100, 150)
    point2 = rg.Point(200, 50)

    # -------------------------------------------------------------------------
    # A RoseGraphics object is not associated with a window,
    # and hence are not drawn, until you ATTACH it to a window.
    # -------------------------------------------------------------------------
    point1.attach_to(window)
    point2.attach_to(window)

    # -------------------------------------------------------------------------
    # And they still are not DRAWN until you RENDER the window.
    # That will draw ALL the objects on the window.
    # This two-step approach is important for animation.
    # -------------------------------------------------------------------------
    window.render()

    window.close_on_mouse_click()


def example3():
    """Displays a Circle and a Rectangle."""
    # -------------------------------------------------------------------------
    # RoseWindow: optionally takes its width and height.
    # -------------------------------------------------------------------------
    width = 700
    height = 400
    window = rg.RoseWindow(width, height)

    # -------------------------------------------------------------------------
    # Circle: needs its center and radius.
    # Has  fill_color  instance variable.
    # -------------------------------------------------------------------------
    center_point = rg.Point(300, 100)
    radius = 50
    circle = rg.Circle(center_point, radius)
    circle.fill_color = "green"
    circle.attach_to(window)

    # -------------------------------------------------------------------------
    # Rectangle: needs two opposite corners.
    # -------------------------------------------------------------------------
    point1 = rg.Point(100, 150)
    point2 = rg.Point(200, 50)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.attach_to(window)

    # -------------------------------------------------------------------------
    # render: Draw ALL the objects attached to this window.
    # -------------------------------------------------------------------------
    window.render()

    # -------------------------------------------------------------------------
    # A Rectangle has instance variables  corner_1  and  corner_2.
    # -------------------------------------------------------------------------
    corner1 = rectangle.corner_1
    corner2 = rectangle.corner_2
    print(corner1, corner2)  # You can also PRINT RoseGraphics objects.
    print(rectangle.get_lower_right_corner())
    print(rectangle)  # See the Console for the output.

    # -------------------------------------------------------------------------
    # close_on_mouse_click: Keeps the window open until user clicks.
    # -------------------------------------------------------------------------
    window.close_on_mouse_click()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# This unusual form is necessary for the special testing we provided.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
