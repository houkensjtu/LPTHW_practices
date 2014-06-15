my_name = "Hou Ken"
my_age = 27
my_height = 187
my_weight = 67
my_eyes = "brown"
my_teeth = "white"
my_hair = "black"

print("Let's talk about %s."%my_name)
print("Let's talk about"+my_name)
print("Let's talk about",my_name)

print("He is %d cm tall."%my_height)
print("He is %d kg heavy."%my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair."%(my_eyes,my_hair))
print("His teeth are usually %s depending on the tobacco."%my_teeth)

# This line is tricky, try to get it exactly right
print("If i add %d,%d,and %d I get %d."%(my_age,my_height,my_weight,my_age + my_height + my_weight))

name = "Hou Ken"
age = 27
height = 187
weight = 67
eyes = "brown"
teeth = "white"
hair = "black"

print("Let's talk about %s."%name)
print("Let's talk about"+name)
print("Let's talk about",name)

print("He is %d cm tall."%height)
print("He is %d kg heavy."%weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair."%(eyes,hair))
print("His teeth are usually %s depending on the tobacco."%teeth)

# This line is tricky, try to get it exactly right
print("If i add %d,%d,and %d I get %d."%(age,height,weight,age + height + weight))

# Try sth with %r
print("I don't know if r works well since I am %r old and my name is %r."%(age,name))
