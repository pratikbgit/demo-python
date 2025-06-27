# Returns student as tuple, unpacking it

# def main():
#     name, house = get_student()
#     print(f"{name} from {house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house

# if __name__ == "__main__":
#     main()

def main():
    name, house, street = get_student()
    print(f"{name} from {house} and Street is {street}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    street = input("Street: ")
    return name, house, street

if "__name__" and "__house__":
    main()