# Modularizes getting student's name and house

# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")


# if __name__ == "__main__":
#     main()


def main():
    name = get_name()
    house = get_house()
    street = get_street()

    print(f"{name} from house {house} and street is {street}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")
    
def get_street():
    return input("street: ")

if __name__ == "__main__":
    main()