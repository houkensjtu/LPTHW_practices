from sys import argv

script, file = argv

txt = open(file)

print("Here is your file %r"%file)

print(txt.read())
