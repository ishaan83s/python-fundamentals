#CREATING DICTIONARY

dict = {
    "user" : "Ishaan",
    "age" : 21,
    "studying" : "python",
    "want to learn" : ["Python","DSA" , "BACKEND" ,"AI/ML" , "SYSTEM DESIGN"]
}

#PRINTING DICTIONARY
print(type(dict))
print(dict)

#PRINT/ACCESS A SPECIFIC KEY
print(dict.get("user")) #Prints ishaan , But if instead we use print (dict[key]) it gives error so avoid using it in first place.


#ADD AN ELEMENT TO A DICTIONARY
dict["Email"] = "xyz@gmail.com" #adds a value to the end of the dictionary
print(dict)

#DELETING A KEY
#dict.pop("email")
# above if we dont write none then it will give error
dict.pop("email", None) #here there is no "email" key its "Email" , but since we used ,None it wont be an error
dict.pop("Email", None)
print(dict)

#DICTIONARY NESTING
dict1 = {
    "key1" : "no",
    "key2" : "no",
    "key3" : {
        "key3_1" : "no",
        "key3_2" : "NO"
    }
    ,
    "key4" : ["Spider", "man" , "brand" , "new" , "day", "is" , "coming"]
}

print(dict1)

#HOW TO ACCESS A KEY INSIDE THE NESTED DICTIONARY
print(dict1["key3"]["key3_2"])