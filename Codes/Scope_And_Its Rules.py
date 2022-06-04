#Scope - what variable do I have access to?

if True:
    x = 10

def some_func():
    total = 100
    
# print(total) - gives error as local scope

print(x) # no error as x is in global scope


# Rules of Scope

""" Rule 1. start with local """
a=1

def confusion():
    a =5
    return a

print(confusion()) # prints 5
print(a) # prints 1


""" Rule 2. Look in Parent local scope """

a=1
def parent():
        a = 10
        def confusion():
            return a # looks in parent scope
        return confusion()

print(parent()) # prints 10
print(a) # prints 1


""" Rule 3. Look in Global scope """


a=1
def parent():
        def confusion():
            return a # looks in global scope
        return confusion()

print(parent()) # prints 1
print(a) # prints 1


""" Rule 4. Built in python """

a=1
def parent():
       
        def confusion():
            return sum # looks in parent scope
        return confusion()

print(parent()) # acknowledges sum as built in function
print(a) # prints 1

"""parameters are treated as local variables"""

b = 100
def confusion(b):
    print(b)


confusion(300) #prints 300


""" using global variables as local - though 
not a sugegsted way to use this approach"""

total  = 0

def count():
    global total 
    total += 1
    return total

print(count()) #1
print(count()) #2
print(count()) #3 

# better approach

total = 0

def count(total):
    total += 1
    return total

print(count(count(count(total)))) # prints 3
# here total remains unaffected

print(total) # prints 0


""" non local keyword : introduced in python 3"""

def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)
    
outer()

# here inner and outer both uses same x i.e non local value

def outer():
    x = "local"
    def inner():
        # nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)
    
outer()

#  inner: nonlocal, outer: local







