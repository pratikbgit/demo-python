# Prints column of bricks using a function with a loop


def main():
    print_column(3)
    print_dollar(6)

def print_column(height):
    for _ in range(height):
        print("#")

def print_dollar(dol):
    for _ in range(dol):
        print("$")

main()