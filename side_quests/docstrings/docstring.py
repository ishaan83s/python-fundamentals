def square (n):
    '''Hello this is a docstring''' #the docstrings is like comment but not comment
    #docstring always need to be exactly below the definition of the function, or else it wont work
    return n**2

print(square(2))

#to print our docstring
print(square.__doc__)

#docstrings are used to document our code