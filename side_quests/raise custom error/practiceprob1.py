while True:
    a = input("Enter a number between 6 7 : , or 'quit'")

    if a.lower() == "quit":
        print("BYEEE!")
        break

    try:
        x = float(a)
        if x<6 or x>7:
            raise ValueError("NOT A VALID NUMBER")
        print(f"YOU ENTERED VALID NUMBER {x}")
    
    except Exception as e:
        print(f"Error: {e} occured. Please try again\n")