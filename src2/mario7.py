# Prints square of bricks using a function with a loop and str multiplication


def main():
    # x = int(input("Enter number of rows and column "))
    print_square(3)


def print_square(size):
    for _ in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()