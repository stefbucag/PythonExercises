"""
Script stores the iterative function.

This iterative function returns the sum of elements in a list.
Eg. given the list [1,2,3] the function returns 1+2+3 = 6.
Rewrite it as a recursive function.
"""
from argparse import ArgumentParser


def get_sum(numbers):
    """Return the sum of numbers in the list.

    :param numbers: List of numbers to be added
    :type numbers: list
    :return sum: Sum of the numbers in the list
    :return type: int
    """
    if len(numbers) > 1:
        map(int, args.numbers)
        return numbers[0] + get_sum(numbers[1:])
    else:
        sum = 0 if len(numbers) == 0 else numbers[0]
        return sum

def __get_argparser():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('numbers', help='Numbers to add', nargs='*')

    return parser


if __name__ == '__main__':
    argparser = __get_argparser()
    args = argparser.parse_args()

    sum = get_sum(args.numbers)
    print '{numbers} = {sum}'.format(numbers=args.numbers, sum=sum)
