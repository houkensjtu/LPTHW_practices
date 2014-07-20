def add(a,b):
    print "ADDING %d + %d:"%(a,b)
    return a + b

def substract(a,b):
    print "SUBSTRACTING %d - %d:"%(a,b)
    return a - b

def multiply(a,b):
    print "MULTIPLYING %d x %d:"%(a,b)
    return a*b

def divide(a,b):
    print "DIVIDING %d / %d:"%(a,b)
    return a/b

print "Let's do some math with just functions!"

age = add(30,5)
height = substract(188,1)
weight = multiply(2,23)
iq = divide(100,2)

print "Age:%d, Height:%d, Weight:%d, IQ:%d."%(age,height,weight,iq)

print "Here's a puzzle."

what = add(age, substract(height, multiply(weight,divide(iq,2))))

print "That becomes:",what,"Can you do it by hand?"

print "Or, it could be calculated directly as:%d."% (height - (iq/2)*weight + age)
