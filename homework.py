prompt = 'what is your name'
name = input(prompt)

print("hello "+name)

prompt = 'give the 1st nbr'
a = input(prompt)
a = int(a)
prompt = 'give the 2nd nbr'
b = input(prompt)
b = int(b)
print(int(a/b))

prompt = "give ma the radius of a circle to get the surface"
r = input(prompt)
r = int(r)
import math
print(math.pi*r*r)