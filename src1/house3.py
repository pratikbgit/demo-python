name = input("What's your name? ")

match name:
    case "Pratik" | "Sandeep" | "Rakesh":
        print("Rajkot")
    case "Arjun":
        print("Amreli")
    case _:
        print("Who ?")