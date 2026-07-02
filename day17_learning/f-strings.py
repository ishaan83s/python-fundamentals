#1 THE PROBLEM TRADITIONAL STRING FORMATTING
# letter = "Hey my name is {} and i am in {}" #ONE MORE WAY OF DOING THIS
letter = "Hey my name is {0} and i am in {1}"
name = "Ishaan"
country = "London"

print(letter.format(name,country)) #the name here is 0 and country here is 1 
#but what if there are many variables to be assigned ? 

#so we python 3 came with a new type of string f-string

print(f"Hello my name is {name} and I am in {country}")
#so its better to format like this and efficient