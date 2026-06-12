tring = "NOBODYIEYES"
for char in tring:
    if(char=="O"):
        print("O FOUND")
        break
    print(char)
else: #WHY NEED THIS ELSE? : WHERE WE USE BREAK, WE USE ELSE
    print("end")