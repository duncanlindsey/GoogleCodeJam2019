def IsApproximatelyEqual(x, y, epsilon = 1e-6):
    """Returns True if y is within relative or absolute 'epsilon' of x.

    By default, 'epsilon' is 1e-6.
    """
    # Check absolute precision.
    if -epsilon <= x - y <= epsilon:
        return True

    # Is x or y too close to zero?
    if -epsilon <= x <= epsilon or -epsilon <= y <= epsilon:
        return False

    # Check relative precision.
    return (-epsilon <= (x - y) / x <= epsilon or -epsilon <= (x - y) / y <= epsilon)

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    # This is all you need for most Code Jam problems.
    t = int(input()) # read a line with a single integer
    for i in range(1, t + 1):
      n, m = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
      print("Case #{}: {} {}".format(i, n + m, n * m))
      # check out .format's specification for more formatting options