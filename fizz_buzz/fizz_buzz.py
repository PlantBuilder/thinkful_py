"""v1: Fizz Buzz: Hard coded limit.
 This module simulate Fizz Buzz Game. """

print  "fizz buzz counting up to 100."

for n in range(1, 100):
    if  n%5 == 0 and n%3 == 0:
        print "fizz buzz"
    elif n%3 == 0 or n%5 == 0:
        if n%3 == 0:
            print "fizz"
        else:
            print "buzz"
    else:
        print n
