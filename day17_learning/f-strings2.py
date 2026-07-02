txt = "for only {price:.2f} dollars" #2f is numbers till 2 decimal points #and rounds off
price = 2.99999999990182

print(txt.format(price = price)) #here we needed to map price = price
#cuz we mentioned "price:.2f" inside the string not an empty space 
#if empty space it wouldve assigned itself

#better method 
print(f"for only {price:.2f} dollars") #prints the same w minimal lines