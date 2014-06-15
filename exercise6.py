x = "There are %d types of people."%10
binary = "binary"
do_not = "don't"
# A combination of 2 %s -> %(... , ...)
y = "Those who know %s and those who %s."%(binary,do_not)

print x
print y

print "I said: %r."%x
print "I also said: '%s'."%y
print "I also said: %s."%y
print "I also said: %r."%y

# False is built-in boolean value...
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# format string using variables
print joke_evaluation %hilarious

w = "This is the left side of..."
e = "a string with a right side."

# Combination of two strings
print w + e
