"""v2: Fizz Buzz: Command line limit.
 This module simulate Fizz Buzz Game. """
import sys

FLAG = True
while FLAG:
    try:
        if len(sys.argv) > 1:
            RANGE_END = int(sys.argv[1])
            break
    except ValueError:
        print "Input was not an integer..."
        FLAG = False

    try:
        FLAG = True
        RANGE_END = raw_input("Please enter an integer: ")
        RANGE_END = int(RANGE_END)
        break
    except ValueError:
        print "Please enter an integer ..."

print  "fizz buzz counting up to " + str(RANGE_END)
for n in range(1, int(RANGE_END)):
    if  n%5 == 0 and n%3 == 0:
        print "fizz buzz"
    elif n%3 == 0 or n%5 == 0:
        if n%3 == 0:
            print "fizz"
        else:
            print "buzz"
    else:
        print n
