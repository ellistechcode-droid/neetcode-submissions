from types import NoneType


def divide_numbers(a: int, b: int) -> None:
    try:
        return print(a / b)
    except:
        print("An error occurred!")



# do not modify below this line
divide_numbers(10, 2)
divide_numbers(12, 3)
divide_numbers(2, 0)
