from Necklace.necklace import *
import sys


usage = f"""
alpha-Necklace-Splitting
------------------------
Usage: 

    python {__file__} [necklace] [alpha]

    Arguments:
    necklace (optional):        a string or comma separated list of numbers representing the necklace.
    alpha (optional):           a commma separated list of numbers, representing the alpha vector.
                                The order is the same as the order how the letters/numbers occurr in your necklace.
                                This argument is required if [necklace] is set.

    Flags:
    --help, -h:     print this help message and exit

Description:

    This program solves alpha-Necklace-Splitting on a given necklace and a vector alpha.
    You can solve alpha-Necklace-Splitting on a necklace using two options:

        1) Interactive mode, the program will ask you to input all the necessary arguments when it needs them.
        2) Specifying a necklace and an alpha vector as command line arguments.

    Interactive mode is invoked when no command line arguments are given.
    Otherwise, the program assumes the necklace and alpha-vector being specified as command line arguments.

Example:

    python {__file__} aaabbaacccc 1,2,3

The necklace is 'aaabbaacccc' and the alpha is given as 'alpha[a] = 1, alpha[b] = 2, alpha[c] = 3'.

"""


def solve(neckl, alpha):
    print("Solving alpha-necklace splitting...")
    try:
        alphaCut, negAlphaCut = neckl.findAlphaCut(alpha)
        print(f"Found Alpha Cut: {alphaCut}")
        neckl.displayCut(alphaCut)
        print()
        print(f"Found Negalpha Cut: {negAlphaCut}")
        neckl.displayCut(negAlphaCut)
    except ValueError as err:
        print(err)
    except AssertionError:
        print(f"Something went wrong. Is your necklace n-separable?")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")


for x in sys.argv:
    if "-h" in x:
        print(usage)
        exit()

if len(sys.argv) < 2:
    print("You are now in interactive mode. (Use --help for a usage information)")
    print("Enter your necklace as a string or a comma separated list of numbers.")
    try:
        neckl_input = input("Necklace: ")
        if "," in neckl_input:
            neckl_input = neckl_input.split(",")
            neckl_input = [int(x) for x in neckl_input]
        neckl = Necklace(neckl_input)
    except:
        print("Something went wrong. Does your input have the correct format?")
        exit()

    try:
        alpha = {}
        print(
            "Now input your alpha-vector. You will be asked for each type separately."
        )
        for letter in neckl.typeIndex:
            alpha[letter] = int(input(f"Input alpha[{letter}]: "))
    except:
        print("Something went wrong. Did you input only numbers?")
        exit()
    print()
    solve(neckl, alpha)
    exit()
elif len(sys.argv) != 3:
    print(usage)
    exit()
else:
    print(
        "You specified the necklace and the alpha-vector as command line arguments. (Use --help for a usage information)"
    )
    try:
        neckl_input = sys.argv[1]
        neckl = Necklace(neckl_input)
        alpha_input = sys.argv[2].split(",")
        alpha_input = [int(x) for x in alpha_input]
        alpha = {}
        for letter in neckl.typeIndex:
            alpha[letter] = alpha_input[neckl.typeIndex[letter]]
    except:
        print("Something went wrong. Does your input have the correct format?")
        exit()
    print()
    solve(neckl, alpha)
    exit()
