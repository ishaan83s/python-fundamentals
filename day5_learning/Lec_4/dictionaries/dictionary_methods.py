mydict = {
    "key1" : "spiderman",
    "key2" : "ironman",
    "key3" : "captain america",
    "dcheroes" : {
        "dc1" : "superman" ,
        "dc2" : "aquaman" ,
    },
    "FAV SUPERHERO" : "DAMON SALVATORE"

}

#RETURN ALL THE KEYS (BUT NOT THE SUBKEYS)
print(mydict.keys())

#RETURN ALL THE VALUES (PRINTS ALL THE VALUES EVEN IN SUBKEYS OF NEST)
print(mydict.values())

#RETURNS ALL THE (key,value) PAIRS AS A TUPLE
print(mydict.items())

#RETURNS THE VALUE ACCORDING TO THE KEY
print(mydict.get("FAV SUPERHERO", None))

#ADDS AN ELEMENT OR A DICTIONARY TO THE DICTIONARY
mydict.update({"mota":"vivaan" , "chomu" : "jay"})

print(mydict)

#WE CAN CONVERT A DICTIONARY INTO ANY ANY ANY DATA STRUCTURE 

#LIST
print(list(mydict)) #THIS ALSO RETURNS KEYS SAME AS MYDICT.KEYS
print(list(mydict.values()))
print(list(mydict.keys()))

#SAME FOR TUPLE