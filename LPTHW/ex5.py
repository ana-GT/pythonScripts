# -- coding: utf-8 --

# ************************************
# ex5.py: More Variables and Printing
# ************************************

my_name = 'V.Lutvenn'
my_age = 26 # Not a lie
my_height = 63 # inches
my_weight = 115 # Yes, I am slimming down
my_eyes = 'Brown'
my_teeth = 'White' # Bless toothpaste!
my_hair = 'Black'

print "Let's talk about %s." %my_name
print "She is %d inches tall." %my_height
print "She is %d pounds heavy." %my_weight
print "actually, that is not too heavy, she was fatter before"
print "She got %s eyes and %s hair." %(my_eyes, my_hair)
print "Her teeth are usually %s depending on the coffee" %my_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight )
