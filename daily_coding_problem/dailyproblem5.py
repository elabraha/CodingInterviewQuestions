# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and
# last element of that pair. For example, car(cons(3, 4)) returns 3, and
# cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
#
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
#
# Implement car and cdr.

# Not sure what f() is for above maybe it's to name the tuple?? I can do that
# Without naming the tuple. not sure why it's necessary to define it like that
# at all in python. The method above is confuusing and rather weird maybe that's
# why this is a coding problem?? Who knows, I'll do it both ways

def cons(a, b):
    return (a, b)

def cdr(p):
    return p[-1]

def car(p):
    return p[0]

# With that weird pair method: (again this is a very weird problem)
# I guess it's to see if you know how function calling works
# It's harder than you think.
# I had to get help with this one becuase I wasn't really getting it
# but what it seems to be getting at is that cons defines a function
# that recieves a function pair(f) f is also a function that is not defined in
# cons or pair but called in pair and then returned and then pair is then returned
# so then in order to get a from the created pair back you would need to match
# what was returne from cons, a function that calls another function,
# you then define another function much like f(a, b) that takes 2 arguments and
# returns the first one, doesn't even matter what you call any of the variable
# because what you received was just a function object that you now must call
# you know that it requires another funtion that it will call when you run it
# by calling name_of_function(func_object_you_just_defined). now since you already
# conveniently defined a function that gives it what you want you call the function
# as stated before and it will run your proposed function.
# It's a very weird thing to think about because cons depends on another
# function to work, cons wont work without ca ror cdr, cdr and car won't work
# without cons

def cons_(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car_(pair):
    def f(a, b):
        return a
    return pair(f)

def cdr_(pair):
    def f(a, b):
        return b
    return pair(f)

def main():
    print("cdr:", cdr(cons(3,4)), "car:", car(cons(3,4)))
    print("weird car:", car_(cons_(3, 4)), "weird cdr:", cdr_(cons_(3, 4)))
main()
