"""
Webby numbers are those whose only prime factors are 5, 3 or 2. The sequence
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24 shows the
first 15 Webby numbers. Write a python program to print the 1200'th
number in the sequence. A good solution should execute in < 1 second.
"""
import time
from argparse import ArgumentParser

def __weeby(num):
    # List comprehension of numbers divisible by 2,3 or 5.
    weeby = (num % 2 == 0 or num % 3 == 0 or num % 5 == 0)

    return weeby

def run(n):
    """Run application to get the nth order of the sequence.

    :param n: Order in the sequence
    :type n: int
    :return number: The nth number of the sequence
    :return type: int
    """
    start_time = time.time()
    weeby_sequence = [num for num in list(xrange(1, 1000)) if __weeby(num)]
    number = weeby_sequence[n-1]

    print '{order}th of the sequence: {number}'.format(number=number, order=n)

    total_run_time = time.time()-start_time
    print 'Total Run time: {total_time}s'.format(total_time=total_run_time)


def __get_argparser():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('n', help='order', type=int)

    return parser


if __name__ == '__main__':
    argparser = __get_argparser()
    args = argparser.parse_args()

    run(args.n)
